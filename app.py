
import streamlit as st
from PIL import Image
from supabase_utils import load_recipes, save_recipe, update_recipe, delete_recipe, upload_image

# Ikoner
icons = {
    "book": "icons/book.png",
    "add": "icons/add.png",
    "TeaTime": "icons/TeaTime.png"
}

# Layout & design
st.set_page_config(layout="wide", page_title="My Recipe Book", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
        [data-testid="stSidebar"] { display: none !important; }
        [data-testid="collapsedControl"] { display: none !important; }
        #MainMenu, header, div[data-testid="stToolbar"] { display: none !important; }
        section > div:first-child button[title="Open sidebar"] { display: none !important; }
    </style>
""", unsafe_allow_html=True)

# Navigation
if "page" not in st.session_state:
    st.session_state.page = "home"

with st.container():
    col1, col2, col3 = st.columns([2, 4, 1])
    with col1:
        st.image(icons["TeaTime"], width=400)

if st.session_state.page == "home":
    st.subheader("My Recipe Book")

col1, col2, col3 = st.columns([0.2, 0.2, 1])
with col1:
    if st.button("Add New Recipe"):
        st.session_state.page = "add"
with col2:
    if st.button("My Recipe Book"):
        st.session_state.page = "list"

# Page logic


if st.session_state.page == "add":
    with st.container():
        col1, col2 = st.columns([0.2, 2])
        with col1:
            st.image(icons["add"], width=50)
        with col2:
            st.subheader("Add a New Recipe")

    with st.form("recipe_form"):
        title = st.text_input("Recipe Title")
        ingredients = st.text_area("Ingredients (one per line)")
        instructions = st.text_area("Instructions")
        image_file = st.file_uploader("Upload a Recipe Photo", type=["png", "jpg", "jpeg"])

        col1, col2, col3 = st.columns([2, 2, 2])
        with col2:
            submitted = st.form_submit_button("Save Recipe")

        if submitted and title and ingredients and instructions:
            try:
                image_url = upload_image(image_file) if image_file else ""
                save_recipe(title.strip(), ingredients.strip(), instructions.strip(), image_url)
                st.success(f"✅ Recipe '{title}' saved!")
            except Exception as e:
                st.error(f"❌ Error saving recipe: {e}")

elif st.session_state.page == "list":
    with st.container():
        col1, col2 = st.columns([0.2, 2])
        with col1:
            st.image(icons["book"], width=50)
        with col2:
            st.subheader("My Recipes")

    recipes = load_recipes()

    if not recipes:
        st.info("No recipes found.")
    else:
        search_query = st.text_input("Search by title or ingredients", "")
        sort_order = st.radio("Sort recipes:", ["A → Z", "Z → A"], horizontal=True)
        ascending = sort_order == "A → Z"

        filtered = [r for r in recipes if search_query.lower() in r["title"].lower() or search_query.lower() in r["ingredients"].lower()]
        filtered = sorted(filtered, key=lambda x: x["title"], reverse=not ascending)

        for r in filtered:
            with st.expander(r["title"]):
                if r["image_url"]:
                    st.image(r["image_url"], width=400)
                st.markdown("**Ingredients:**")
                for ing in r["ingredients"].splitlines():
                    st.write(f"- {ing.strip()}")
                st.markdown("**Instructions:**")
                st.write(r["instructions"])

                col1, col2 = st.columns([1, 1])
                with col1:
                    if st.button("Edit", key=f"edit_{r['id']}"):
                        st.session_state.page = "edit"
                        st.session_state.edit_data = r
                with col2:
                    if st.button("Delete", key=f"delete_{r['id']}"):
                        st.session_state.confirm_delete_id = r["id"]
                        st.rerun()

            if st.session_state.get("confirm_delete_id") == r["id"]:
                st.warning(f"Are you sure you want to delete **{r['title']}**?")
                col_del1, col_del2 = st.columns([1, 1])
                with col_del1:
                    if st.button("Yes, delete", key=f"confirm_{r['id']}"):
                        delete_recipe(r["id"])
                        st.success(f"Deleted '{r['title']}'")
                        del st.session_state["confirm_delete_id"]
                        st.rerun()
                with col_del2:
                    if st.button("Cancel", key=f"cancel_{r['id']}"):
                        del st.session_state["confirm_delete_id"]
                        st.rerun()

elif st.session_state.page == "edit":
    r = st.session_state.get("edit_data")
    if not r:
        st.warning("⚠️ No recipe selected to edit.")
    else:
        with st.container():
            col1, col2 = st.columns([0.2, 2])
            with col1:
                st.image(icons["add"], width=50)
            with col2:
                st.subheader("Edit Recipe")

        with st.form("edit_form"):
            title = st.text_input("Recipe Title", value=r["title"])
            ingredients = st.text_area("Ingredients (one per line)", value=r["ingredients"])
            instructions = st.text_area("Instructions", value=r["instructions"])
            image_file = st.file_uploader("Replace Recipe Photo (optional)", type=["png", "jpg", "jpeg"])

            submitted = st.form_submit_button("Update Recipe")

            if submitted and title and ingredients and instructions:
                try:
                    image_url = upload_image(image_file) if image_file else r["image_url"]
                    update_recipe(r["id"], title.strip(), ingredients.strip(), instructions.strip(), image_url)
                    st.success(f"✅ Updated '{title}'!")
                    st.session_state.page = "list"
                    st.rerun()
                except Exception as e:
                    st.error(f"❌ Error updating recipe: {e}")
