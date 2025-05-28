import streamlit as st
from PIL import Image
from ui_utils import hide_page_from_sidebar

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

hide_page_from_sidebar("Edit Recipe")

st.markdown("""
    <style>
        /* Dölj endast sidomenylänken till "Edit Recipe" */
        section[data-testid="stSidebar"] ul li a:has(span:contains("Edit Recipe")) {
            display: none !important;
        }
    </style>
""", unsafe_allow_html=True)

icons = {
    "TeaTime": "icons/TeaTime.png",
    "book": "icons/book.png",
    "add": "icons/add.png"
}

col1, col2, col3 = st.columns([1,4,6])
with col2:
    st.image(icons["TeaTime"], width=400)
#st.markdown("<h1 style='text-align: center;'>My Recipe Book</h1>", unsafe_allow_html=True)

    st.subheader("My Recipe Book")
    if st.button("Add New Recipe"):
        st.switch_page("pages/Add New Recipe.py")
    if st.button("My Recipe Book"):
        st.switch_page("pages/My Recipe Book.py")

##WORKS
#with st.container():
    #col1, col2, col3 = st.columns([3, 2, 3]) 
    #with col1:
        #if st.button("Add New Recipe"):
            #st.switch_page("pages/Add New Recipe.py")
    #with col3:
        #if st.button("My Recipe Book"):
            #st.switch_page("pages/My Recipe Book.py")


#st.page_link("pages/Add New Recipe.py", label="Add New Recipe")
#st.page_link("pages/My Recipe Book.py", label="My Recipe Book")
