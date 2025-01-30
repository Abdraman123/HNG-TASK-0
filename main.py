import os
import uvicorn
from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/")
def get_info():
    return {
        "email": "ajaniabdulrahman@gmail.com",
        "current_datetime": datetime.utcnow().isoformat() + "Z",
        "github_url": "https://github.com/Abdraman123/HNG-TASK-0"
    }

# ✅ Use Railway's assigned port or default to 8000
PORT = int(os.getenv("PORT", 8000))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=PORT)


