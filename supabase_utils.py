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
        print("No file uploaded.")
        return ""

    ext = os.path.splitext(file.name)[1]
    filename = f"{uuid4()}{ext}"
    file_path = f"{filename}"
    print(f"Uploading image: {file_path}")

    res = supabase.storage.from_(BUCKET_NAME).upload(file=file_path, file_data=file, content_type=file.type)
    print("Upload response:", res)
    
    public_url = supabase.storage.from_(BUCKET_NAME).get_public_url(file_path)
    print("Public URL:", public_url)

    return public_url

def save_recipe(title, ingredients, instructions, image_url=""):
    """Insert a recipe into the Supabase DB"""
    data = {
        "title": title,
        "ingredients": ingredients,
        "instructions": instructions,
        "image_url": image_url,
        "created_at": datetime.datetime.utcnow().isoformat()
    }
    print("Saving recipe:", data)
    response = supabase.table("recipes").insert(data).execute()
    print("Insert response:", response)
    
    supabase.table("recipes").insert(data).execute()

def load_recipes():
    """Fetch all recipes from Supabase"""
    response = supabase.table("recipes").select("*").order("title", desc=False).execute()
    return response.data
