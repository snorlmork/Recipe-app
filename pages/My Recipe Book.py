# --- View Recipes Page ---
import streamlit as st
from supabase_utils import load_recipes
from PIL import Image

icons = {
    "book": "icons/book.png",
    "add": "icons/add.png"
}


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