import streamlit as st

st.set_page_config(page_title="Recipe Book", layout="centered")
st.title("Recipe Book")

menu = st.sidebar.selectbox("Navigate", ["Add Recipe", "View Recipes"])

st.subheader("Vad vill du göra?")
st.page_link("pages/Add Recipe.py", label="Add New Recipe")
st.page_link("pages/View Recipies.py", label="My Recipe Book")
