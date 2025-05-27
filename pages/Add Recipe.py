# --- Add Recipe Page ---
import streamlit as st
from supabase_utils import upload_image, save_recipe

menu = st.sidebar.selectbox("Navigate", ["Add Recipe", "View Recipes"])

if menu == "Add Recipe":
    st.subheader("➕ Add a New Recipe")

    with st.form("recipe_form"):
        title = st.text_input("Recipe Title")
        ingredients = st.text_area("Ingredients")
        instructions = st.text_area("Instructions")
        image_file = st.file_uploader("Upload a Recipe Photo", type=["png", "jpg", "jpeg"])
        submitted = st.form_submit_button("Save Recipe")

        if submitted and title and ingredients and instructions:
            try:
                image_url = upload_image(image_file) if image_file else ""
                save_recipe(title.strip(), ingredients.strip(), instructions.strip(), image_url)
                st.success(f"✅ Recipe '{title}' saved!")
            except Exception as e:
                st.error(f"❌ Error saving recipe: {e}")