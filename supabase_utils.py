from supabase import create_client, Client
from uuid import uuid4
import datetime
import os

# Add your Supabase credentials here
SUPABASE_URL = "https://ykmzmmndytgbrejmgkwu.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InlrbXptbW5keXRnYnJlam1na3d1Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDgyODM0MzYsImV4cCI6MjA2Mzg1OTQzNn0.iSGIh_Wxk6zCdSY37YEaHIhEoNbrFLKpwE1cMam8q0w"

BUCKET_NAME = "recipe-images"

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def upload_image(file):
    """Upload image to Supabase Storage and return public URL"""
    if not file:
        return ""

    ext = os.path.splitext(file.name)[1]
    filename = f"{uuid4()}{ext}"
    file_path = f"{filename}"
    print(f"Uploading image: {file_path}")

    file_bytes = file.read()  # Read the UploadedFile as bytes

    supabase.storage.from_(BUCKET_NAME).upload(file_path, file_bytes, {"content-type": file.type})
    public_url = supabase.storage.from_(BUCKET_NAME).get_public_url(file_path)

    return public_url

def save_recipe(title, ingredients, instructions, image_url=""):
    """Insert a recipe into the Supabase DB"""
    import json

    data = {
        "title": title,
        "ingredients": ingredients,
        "instructions": instructions
    }
    if image_url:
        data["image_url"] = image_url

    print("📝 Recipe payload:\n", json.dumps(data, indent=2))

    try:
        response = supabase.table("recipes").insert(data).execute()
        print("📥 Insert response:", response)
        return response
    except Exception as e:
        print("❌ Exception in save_recipe:", e)
        raise

def load_recipes():
    """Fetch all recipes from Supabase"""
    response = supabase.table("recipes").select("*").order("title", desc=False).execute()
    return response.data
