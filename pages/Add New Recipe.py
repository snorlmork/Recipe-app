# --- Add Recipe Page ---
import streamlit as st
from supabase_utils import upload_image, save_recipe
from PIL import Image

icons = {
    "book": "icons/book.png",
    "add": "icons/add.png"
}


with st.container():
    col1, col2 = st.columns([0.2, 2])
    with col1:
        st.image(icons["add"], width=50)
    with col2:
        st.subheader("Add a New Recipe")

with st.form("recipe_form"):
    title = st.text_input("Recipe Title")
    ingredients = st.text_area("Ingredients")
    instructions = st.text_area("Instructions")
    image_file = st.file_uploader("Upload a Recipe Photo", type=["png", "jpg", "jpeg"])
    col1, col2, col3 = st.columns([2,2,2])
    with col2:
        submitted = st.form_submit_button("Save Recipe")

    if submitted and title and ingredients and instructions:
        try:
            image_url = upload_image(image_file) if image_file else ""
            save_recipe(title.strip(), ingredients.strip(), instructions.strip(), image_url)
            st.success(f"✅ Recipe '{title}' saved!")
        except Exception as e:
            st.error(f"❌ Error saving recipe: {e}")