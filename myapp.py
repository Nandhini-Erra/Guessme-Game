import streamlit as st
import sqlite3
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import numpy as np

# ---------------- CONFIG ----------------
st.set_page_config(page_title="Smart Volunteer Connect", layout="wide")

# ---------------- DATABASE ----------------
conn = sqlite3.connect("data.db", check_same_thread=False)
c = conn.cursor()

c.execute('''
CREATE TABLE IF NOT EXISTS users (
    username TEXT,
    password TEXT,
    role TEXT
)
''')

c.execute('''
CREATE TABLE IF NOT EXISTS reports (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    location TEXT,
    issue TEXT,
    urgency TEXT,
    status TEXT,
    assigned_to TEXT
)
''')
conn.commit()

# ---------------- DEFAULT USERS ----------------
def create_users():
    users = c.execute("SELECT * FROM users").fetchall()
    if len(users) == 0:
        default = [
            ("admin", "123", "Admin"),
            ("worker", "123", "Field Worker"),
            ("volunteer", "123", "Volunteer")
        ]
        c.executemany("INSERT INTO users VALUES (?, ?, ?)", default)
        conn.commit()

create_users()

# ---------------- AI MODEL ----------------
def train_model():
    # sample training data
    X = [
        [1, 3], [2, 2], [3, 1], [1, 1], [3, 3], [2, 3]
    ]
    y = [1, 0, 0, 1, 1, 0]  # 1 = high risk

    model = RandomForestClassifier()
    model.fit(X, y)
    return model

model = train_model()

def predict_risk(issue, urgency):
    issue_map = {"Food":1, "Medical":2, "Education":3}
    urgency_map = {"Low":1, "Medium":2, "High":3}

    pred = model.predict([[issue_map[issue], urgency_map[urgency]]])
    return "High Risk" if pred[0] == 1 else "Normal"

# ---------------- SESSION ----------------
if "user" not in st.session_state:
    st.session_state.user = None

st.title("🤝 Smart Volunteer Connect")

# ---------------- AUTH SYSTEM ----------------
auth_mode = st.radio("Select Option", ["Login", "Sign Up"])

if st.session_state.user is None:

    # -------- LOGIN --------
    if auth_mode == "Login":
        st.subheader("🔐 Login")

        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            user = c.execute(
                "SELECT * FROM users WHERE username=? AND password=?",
                (username, password)
            ).fetchone()

            if user:
                st.session_state.user = user
                st.success("Login Successful")
                st.rerun()
            else:
                st.error("Invalid credentials")

    # -------- SIGN UP --------
    elif auth_mode == "Sign Up":
        st.subheader("📝 Create Account")

        new_user = st.text_input("Username")
        new_pass = st.text_input("Password", type="password")
        role = st.selectbox("Select Role", ["Field Worker", "Volunteer"])

        if st.button("Register"):
            existing = c.execute(
                "SELECT * FROM users WHERE username=?",
                (new_user,)
            ).fetchone()

            if existing:
                st.warning("User already exists")
            else:
                c.execute(
                    "INSERT INTO users VALUES (?, ?, ?)",
                    (new_user, new_pass, role)
                )
                conn.commit()

                st.success("Account created! Please login.")

# ---------------- MAIN APP ----------------
else:
    username, password, role = st.session_state.user

    st.sidebar.success(f"{role} - {username}")

    if st.sidebar.button("Logout"):
        st.session_state.user = None
        st.rerun()

    menu = st.sidebar.radio("Menu", ["Dashboard", "Submit Report", "View Cases", "Map", "My Tasks"])

    df = pd.read_sql("SELECT * FROM reports", conn)

    # ---------------- FIELD WORKER ----------------
    if role == "Field Worker":

        if menu == "Submit Report":
            st.header("📋 Submit Report")

            with st.form("form"):
                name = st.text_input("Name")
                location = st.text_input("Location")
                issue = st.selectbox("Issue", ["Food", "Medical", "Education"])
                urgency = st.selectbox("Urgency", ["Low", "Medium", "High"])

                if st.form_submit_button("Submit"):
                    assigned = issue + " Volunteer"
                    c.execute("INSERT INTO reports (name, location, issue, urgency, status, assigned_to) VALUES (?, ?, ?, ?, ?, ?)",
                              (name, location, issue, urgency, "Pending", assigned))
                    conn.commit()

                    st.success("Report Submitted!")

        elif menu == "Dashboard":
            st.metric("Total Reports", len(df))

    # ---------------- ADMIN ----------------
    elif role == "Admin":

        if menu == "Dashboard":
            st.header("📊 Dashboard")

            col1, col2, col3 = st.columns(3)
            col1.metric("Total", len(df))
            col2.metric("High Priority", len(df[df["urgency"] == "High"]))
            col3.metric("Completed", len(df[df["status"] == "Completed"]))

            st.bar_chart(df["issue"].value_counts())

        elif menu == "View Cases":
            st.header("📋 Cases")

            for _, row in df.iterrows():
                risk = predict_risk(row["issue"], row["urgency"])

                st.markdown(f"""
                ### 👤 {row['name']}
                📍 {row['location']}  
                ⚠ {row['issue']} | 🔥 {row['urgency']}  
                🤖 AI: {risk}
                """)

                if risk == "High Risk":
                    st.error("⚠ AI Detected High Risk")

                st.markdown("---")

    # ---------------- MAP ----------------
    elif menu == "Map":
        st.header("📍 Map View")

        map_data = pd.DataFrame({
            "lat": [17.3850, 16.5062, 17.6868],
            "lon": [78.4867, 80.6480, 83.2185]
        })

        st.map(map_data)

    # ---------------- VOLUNTEER ----------------
    elif role == "Volunteer":

        if menu == "My Tasks":
            st.header("🧑‍🤝‍🧑 Tasks")

            tasks = df[df["status"] != "Completed"]

            for _, row in tasks.iterrows():
                st.write(f"{row['location']} | {row['issue']} | {row['urgency']}")

                col1, col2 = st.columns(2)

                if col1.button(f"Accept {row['id']}"):
                    c.execute("UPDATE reports SET status='Accepted' WHERE id=?", (row['id'],))
                    conn.commit()
                    st.rerun()

                if col2.button(f"Complete {row['id']}"):
                    c.execute("UPDATE reports SET status='Completed' WHERE id=?", (row['id'],))
                    conn.commit()
                    st.rerun()