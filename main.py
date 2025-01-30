import os
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

app = FastAPI()
# Enable CORS (Cross-Origin Resource Sharing)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all domains
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# API Endpoint
@app.get("/")
def get_info():
    return {
        "email": "ajaniabdulrahman@gmail.com",  # Replace with your actual email
        "current_datetime": datetime.utcnow().isoformat() + "Z",
        "github_url": "https://github.com/Abdraman123/HNG-TASK-0"  # Replace with your GitHub repo URL
    }
# ✅ Use Railway's assigned port or default to 8000
PORT = int(os.getenv("PORT", 8000))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=PORT)
