import streamlit as st
from PIL import Image

icons = {
    "book": "icons/book.png",
    "add": "icons/add.png"
}

st.set_page_config(page_title="My Recipe Book", layout="centered")
st.markdown("<h1 style='text-align: center;'>My Recipe Book</h1>", unsafe_allow_html=True)

#st.title("My Recipe Book")

#left, right = st.columns(2)
#if left.button("Add New Recipe"):
    #st.switch_page("pages/Add New Recipe.py")
    
#if right.button("My Recipe Book"):
    #st.switch_page("pages/My Recipe Book.py")

with st.container():
    col1, col2, col3 = st.columns([3, 2, 3]) 
    with col1:
        if st.button("Add New Recipe"):
            st.switch_page("pages/Add New Recipe.py")
    with col3:
        if st.button("My Recipe Book"):
            st.switch_page("pages/My Recipe Book.py")

#st.page_link("pages/Add New Recipe.py", label="Add New Recipe")
#st.page_link("pages/My Recipe Book.py", label="My Recipe Book")
