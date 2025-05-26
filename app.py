import streamlit as st
from supabase_utils import upload_image, save_recipe, load_recipes

st.set_page_config(page_title="🍽️ Recipe Book with Supabase", layout="centered")
st.title("🍽️ Cloud Recipe Book")

menu = st.sidebar.selectbox("Navigate", ["Add Recipe", "View Recipes"])

# --- Add Recipe Page ---
if menu == "Add Recipe":
    st.subheader("➕ Add a New Recipe")

    with st.form("recipe_form"):
        title = st.text_input("Recipe Title")
        ingredients = st.text_area("Ingredients (comma-separated)")
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


# --- View Recipes Page ---
elif menu == "View Recipes":
    st.subheader("📖 Saved Recipes")

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
                st.markdown(f"**Ingredients:** {r['ingredients']}")
                st.markdown("**Instructions:**")
                st.write(r["instructions"])
