from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
import pytz

# Create a FastAPI instance
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
        "current_datetime": datetime.now(pytz.utc).isoformat(),
        "github_url": "https://github.com/yourusername/your-repo"  # Replace with your GitHub repo URL
    }

