import streamlit as st

st.set_page_config(page_title="Recipe Book", layout="centered")
st.title("Recipe Book")

st.page_link("pages/Add New Recipe.py", label="Add New Recipe")
st.page_link("pages/My Recipe Book.py", label="My Recipe Book")
