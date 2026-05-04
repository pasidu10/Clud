from fastapi import FastAPI
from mangum import Mangum
from supabase import create_client, Client
from pydantic import BaseModel
from typing import Optional

# FastAPI App එක හදමු
app = FastAPI(title="PASIYA Cloud API", version="1.0.0")

# Vercel එකට අවශ්‍ය Handler එක
handler = Mangum(app)

# ඔයාගේ Supabase විස්තර
SUPABASE_URL = "https://edpwkqwqf64mfa604hom.supabase.co"
SUPABASE_KEY = "sb_publishable_edpwkq-Wqf64MFA604HomA__XbLpIvP"
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Data Schema එක (Register වෙද්දී එන දත්ත)
class UserRegister(BaseModel):
    username: str
    email: str
    password: str

@app.get("/")
def home():
    return {
        "status": "Online",
        "project": "PASIYA Cloud",
        "owner": "PASIYA",
        "message": "Backend is running successfully!"
    }

@app.post("/register")
async def register(user: UserRegister):
    try:
        # Supabase එකේ 'users' table එකට data ඇතුළත් කිරීම
        response = supabase.table("users").insert({
            "username": user.username,
            "email": user.email,
            "password": user.password
        }).execute()
        
        return {
            "status": "Success",
            "message": "User registered successfully",
            "user_data": response.data
        }
    except Exception as e:
        return {
            "status": "Error",
            "details": str(e)
        }

# API එකේ සෞඛ්‍ය තත්වය බලන්න
@app.get("/health")
def health_check():
    return {"status": "Healthy"}
