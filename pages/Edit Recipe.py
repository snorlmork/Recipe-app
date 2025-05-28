import streamlit as st
from supabase_utils import upload_image, update_recipe
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
        st.subheader("Edit Recipe")

edit_data = st.session_state.get("edit_mode")

if not edit_data:
    st.warning("⚠️ No recipe selected to edit.")
    st.stop()

with st.form("edit_form"):
    title = st.text_input("Recipe Title", value=edit_data["title"])
    ingredients = st.text_area("Ingredients (one per line)", value=edit_data["ingredients"])
    instructions = st.text_area("Instructions", value=edit_data["instructions"])
    image_file = st.file_uploader("Replace Recipe Photo (optional)", type=["png", "jpg", "jpeg"])

    submitted = st.form_submit_button("Update Recipe")

    if submitted and title and ingredients and instructions:
        try:
            image_url = upload_image(image_file) if image_file else edit_data["image_url"]
            update_recipe(edit_data["id"], title.strip(), ingredients.strip(), instructions.strip(), image_url)
            st.success(f"✅ Updated '{title}'!")
            del st.session_state["edit_mode"]
            st.switch_page("pages/My Recipe Book.py")
        except Exception as e:
            st.error(f"❌ Error updating recipe: {e}")
