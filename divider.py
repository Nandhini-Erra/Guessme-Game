import streamlit as st
# st.title("Layouts")
# col1, col2, col3 = st.columns(3)

# with col1:    
#     st.header("Column 1")
#     st.write("This is column 1")
#     st.button("Click me 1")
# with col2:
#     st.header("Column 2")
#     st.write("This is column 2")
#     st.button("Click me 2")
# with col3:
#     st.header("Column 3")
#     st.write("This is column 3")
#     st.button("Click me 3")
 
st.title("containers")
with st.container():
    st.header("Container 1")
    st.write("This is container 1")
    st.button("Click me 1")
with st.container():
    st.header("Container 2")
    st.write("This is container 2")
    st.button("Click me 2")
st.write("This is outside the container")
st.title("Expander")
st.write("Expander details")
with st.expander("See details"):
   st.write("This is the details section")
   st.button("Click me for details")
st.write("Expander details 2")
with st.expander("See details 2"):
   st.write("This is the details section 2")
   st.button("Click me for details 2")
st.title("Sidebar")
st.sidebar.header("Sidebar")
st.sidebar.write("This is the sidebar")
st.sidebar.button("Click me in sidebar")

# tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])
# with tab1:
#     st.header("Tab 1")
#     st.write("This is tab 1")
#     st.button("Click me in Tab 1")
# with tab2:
#     st.header("Tab 2")
#     st.write("This is tab 2")
#     st.button("Click me in Tab 2")
# with tab3:
#     st.header("Tab 3")
#     st.write("This is tab 3")
#     st.button("Click me in Tab 3")
    