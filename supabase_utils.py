from supabase import create_client, Client
from uuid import uuid4
import datetime
import os

# Add your Supabase credentials here
SUPABASE_URL = "https://your-project-id.supabase.co"
SUPABASE_KEY = "your-anon-key"

BUCKET_NAME = "recipe-images"

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def upload_image(file):
    """Upload image to Supabase Storage and return public URL"""
    if not file:
        return ""

    ext = os.path.splitext(file.name)[1]
    filename = f"{uuid4()}{ext}"
    file_path = f"{filename}"

    supabase.storage.from_(BUCKET_NAME).upload(file=file_path, file_data=file, content_type=file.type)
    public_url = supabase.storage.from_(BUCKET_NAME).get_public_url(file_path)

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
    supabase.table("recipes").insert(data).execute()

def load_recipes():
    """Fetch all recipes from Supabase"""
    response = supabase.table("recipes").select("*").order("title", desc=False).execute()
    return response.data
