from fastapi import FastAPI
from mangum import Mangum

app = FastAPI(title="PASIYA Cloud API")
handler = Mangum(app) # Vercel එකට අත්‍යවශ්‍යයි

@app.get("/")
def read_root():
    return {
        "status": "Online",
        "message": "Welcome to PASIYA Cloud Backend",
        "version": "1.0.0"
    }

@app.get("/health")
def health_check():
    return {"status": "Healthy"}
