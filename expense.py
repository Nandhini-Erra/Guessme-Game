import streamlit as st
st.markdown(
    """<style>
    .stApp {
    background-image: url("https://tse3.mm.bing.net/th/id/OIP.oYWU1WkULmhnzPQAC8W5agHaHa?pid=Api&P=0&h=180");
    background-size: cover;
    background-color: pink;
    font-family: 'Arial', sans-serif;
    text-color: black;
    text-align: center;
    }
    </style>""", unsafe_allow_html=True
)
st.set_page_config(page_title="Personal Expense Tracker", page_icon="💰", layout="wide")
st.title("💰Personal Expense Tracker")
st.write("➕Add Expense")
if "expenses" not in st.session_state:
    st.session_state.expenses = []
col1,col2=st.columns(2)
with col1:
    st.header("add new expenses")
    with st.form("expense_form"):
        title=st.text_input("Expense Title")
        amount=st.number_input("Amount", min_value=0)
        category=st.selectbox("Category", ["Food", "Transport", "Entertainment", "Utilities", "Other"])
        add=st.form_submit_button("Add Expense")
        if add:
            st.session_state.expenses.append({"title": title, "amount": amount, "category": category})
            st.success("Expense added successfully!")
with col2:
    st.header("📊Expense summary")
    st.write("Total expenses.")
    total_expense = sum(expense["amount"] for expense in st.session_state.expenses)
    st.write(f"Total expenses: rs{total_expense}")
    show_details = st.toggle("Show details")

    if show_details:
        for item in st.session_state.expenses:
            st.write(f"{item['title']} - rs{item['amount']} ({item['category']})")
    category=st.selectbox("Category ", ["Food", "Transport", "Entertainment", "Utilities", "Other"])
    if category != "All":
        filtered_expense = sum(expense["amount"] for expense in st.session_state.expenses if expense["category"] == category)
        st.write(f"Total expenses for {category}: rs{filtered_expense}")
    else:
        st.warning("Please select a category to filter expenses.")


    


