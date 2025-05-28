# --- View Recipes Page ---
import streamlit as st
from supabase_utils import load_recipes, delete_recipe
from PIL import Image
from ui_utils import hide_page_from_sidebar

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

hide_page_from_sidebar("Edit Recipe")

icons = {
    "book": "icons/book.png",
    "add": "icons/add.png"
}

with st.container():
    col1, col2 = st.columns([0.1, 2.5])
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

     # Filter and sort
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
                    st.session_state["edit_mode"] = r
                    st.switch_page("pages/Edit Recipe.py")
            with col2:
                if st.button("Delete", key=f"delete_{r['id']}"):
                    st.session_state["confirm_delete_id"] = r["id"]
                    st.session_state["confirm_delete_title"] = r["title"]
                    st.rerun()
                    # Visa bekräftelse om användaren klickat "Delete"
            if st.session_state.get("confirm_delete_id") == r["id"]:
                st.warning(f"Are you sure you want to delete **{r['title']}**?")
                col_del1, col_del2 = st.columns([1, 1])
                with col_del1:
                    if st.button("Yes, delete", key=f"confirm_{r['id']}"):
                        delete_recipe(r["id"])
                        st.success(f"Deleted '{r['title']}'")
                        del st.session_state["confirm_delete_id"]
                        del st.session_state["confirm_delete_title"]
                        st.rerun()
                with col_del2:
                    if st.button("Cancel", key=f"cancel_{r['id']}"):
                        del st.session_state["confirm_delete_id"]
                        del st.session_state["confirm_delete_title"]
                        st.rerun()
