import streamlit as st

st.set_page_config(page_title="My Recipe Book", layout="centered")
st.title("My Recipe Book")


if st.button("Add New Recipe"):
    st.switch_page("pages/Add New Recipe.py")
    
if st.button("My Recipe Book"):
    st.switch_page("pages/My Recipe Book.py")

#st.page_link("pages/Add New Recipe.py", label="Add New Recipe")
#st.page_link("pages/My Recipe Book.py", label="My Recipe Book")
