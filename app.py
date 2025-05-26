import streamlit as st
import pandas as pd
import os
import uuid
from PIL import Image

# File paths
CSV_FILE = "recipes.csv"
IMAGE_FOLDER = "images"
os.makedirs(IMAGE_FOLDER, exist_ok=True)

# Load or initialize recipe data
if os.path.exists(CSV_FILE):
    df = pd.read_csv(CSV_FILE)
else:
    df = pd.DataFrame(columns=["Title", "Ingredients", "Instructions", "Image"])

# Streamlit page settings
st.set_page_config(page_title="My Recipe Book", layout="centered")
st.title("🍽️ My Recipe Book")

# Sidebar navigation
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
            image_path = ""

            if image_file:
                ext = os.path.splitext(image_file.name)[1]
                filename = f"{uuid.uuid4()}{ext}"
                image_path = os.path.join(IMAGE_FOLDER, filename)

                # Save image
                with open(image_path, "wb") as f:
                    f.write(image_file.getbuffer())

            new_row = {
                "Title": title.strip(),
                "Ingredients": ingredients.strip(),
                "Instructions": instructions.strip(),
                "Image": image_path
            }

            df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
            df.to_csv(CSV_FILE, index=False)
            st.success(f"✅ Recipe '{title}' saved!")

# --- View Recipes Page ---
elif menu == "View Recipes":
    st.subheader("📖 Saved Recipes")

    if df.empty:
        st.info("No recipes saved yet. Add some!")
    else:
        # Search input
        search_query = st.text_input("Search by title or ingredients", "")

        # Sorting option
        sort_order = st.radio("Sort recipes:", ["A → Z", "Z → A"], horizontal=True)

        # Filter and sort
        filtered_df = df[
            df["Title"].str.contains(search_query, case=False, na=False) |
            df["Ingredients"].str.contains(search_query, case=False, na=False)
        ]

        ascending = sort_order == "A → Z"
        filtered_df = filtered_df.sort_values("Title", ascending=ascending)

        if filtered_df.empty:
            st.warning("No recipes found matching your search.")
        else:
            for i, row in filtered_df.iterrows():
                with st.expander(f"{row['Title']}"):
                    if row["Image"] and os.path.exists(row["Image"]):
                        st.image(row["Image"], width=400)
                    st.markdown(f"**Ingredients:** {row['Ingredients']}")
                    st.markdown("**Instructions:**")
                    st.write(row['Instructions'])