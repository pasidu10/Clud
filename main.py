from fastapi import FastAPI
from supabase import create_client, Client
from pydantic import BaseModel

app = FastAPI()

# Supabase විස්තර
SUPABASE_URL = "https://edpwkqwqf64mfa604hom.supabase.co"
SUPABASE_KEY = "sb_publishable_edpwkq-Wqf64MFA604HomA__XbLpIvP"
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

class UserRegister(BaseModel):
    username: str
    email: str
    password: str

@app.get("/")
def home():
    return {"status": "Online", "owner": "PASIYA"}

@app.post("/register")
async def register(user: UserRegister):
    try:
        response = supabase.table("users").insert({
            "username": user.username,
            "email": user.email,
            "password": user.password
        }).execute()
        return {"message": "Success", "user": response.data}
    except Exception as e:
        return {"message": "Error", "details": str(e)}
