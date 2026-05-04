import os
from fastapi import FastAPI
from supabase import create_client, Client

app = FastAPI()

# Supabase විස්තර (ඔයා එවපු විස්තර මෙතනට දැම්මා)
url: str = "https://edpwkqwqf64mfa604hom.supabase.co" # ඔයාගේ Project ID එකෙන් හැදුණු URL එක
key: str = "sb_publishable_edpwkq-Wqf64MFA604HomA__XbLpIvP" 
supabase: Client = create_client(url, key)

@app.get("/")
def home():
    return {"status": "PASIYA Cloud Backend Online"}

@app.post("/register")
async def register_user(username: str, email: str, password: str):
    response = supabase.table("users").insert({
        "username": username, 
        "email": email, 
        "password": password 
    }).execute()
    return {"message": "User registered successfully", "data": response.data}
