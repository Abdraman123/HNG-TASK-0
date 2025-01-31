# HNG Task 0 - Public API

This is a simple FastAPI-based public API that provides the following information in JSON format:

- Your registered email address.
- The current UTC datetime in ISO 8601 format.
- The GitHub URL of the project's codebase.

The API is **publicly accessible** and deployed using **Railway**.

---

## 🚀 Features
- Accepts `GET` requests at the root endpoint `/`
- Returns **email, current time, and GitHub repo URL** in JSON format.
- Hosted on **Railway** with CORS handling.
- API documentation available via **Swagger UI**.

---

## 🔧 Installation (Run Locally)

Follow these steps to set up and run the project locally:

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/Abdraman123/HNG-TASK-0.git
```
### 2️⃣ Navigate to the Project Folder
```bash
cd HNG-TASK-0
```
### 3️⃣ Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv env
source env/bin/activate  # Mac/Linux
env\Scripts\activate     # Windows
```
### 4️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
### 5️⃣ Run the API Locally
```bash
uvicorn main:app --reload
```
### 6️⃣ Open the API in Your Browser
```
Main API Response: http://127.0.0.1:8000
API Documentation (Swagger UI): http://127.0.0.1:8000/docs
```
## 📡 API Deployment on Railway

This API is deployed on Railway and accessible via:

🔗 Live API Endpoint:
(https://hng-task-0-production-a8d4.up.railway.app/)

🔗 API Documentation (Swagger UI):
(https://hng-task-0-production-a8d4.up.railway.app/docs)
## 🛠 API Documentation
🟢 Endpoint: GET /
✅ Response Format (200 OK)
```
{
  "email": "your-email@example.com",
  "current_datetime": "2025-01-30T22:45:00Z",
  "github_url": "https://github.com/Abdraman123/HNG-TASK-0"
}
```
🔹 Make sure to replace "your-email@example.com" with your actual email.

## 🚀 Deployment Guide (Using Railway)
Follow these steps to deploy the API on Railway:

### 1️⃣ Push Your Code to GitHub
```bash
git add .
git commit -m "Initial commit with FastAPI setup"
git push origin main
```
###2️⃣ Create a New Project on Railway
Go to Railway.app
Click "New Project" → "Deploy from GitHub Repository"
Select your HNG-TASK-0 repository.

###3️⃣ Configure Environment Variables
In Railway Dashboard, go to Settings → Environment Variables.
Add the following variable:
```
PORT = 8000
```
### 4️⃣ Deploy the Application
Click Deploy and wait for the process to complete.
Once deployed, Railway will provide a public URL.

### 5️⃣ Test the API
Open your public URL in a browser to check if the API is running.
Visit /docs to see the API documentation.

## 🔍 Verifying Deployment & GitHub Sync
To check if your code is successfully uploaded to GitHub, run:
```bash
git status
```
If everything is up to date, you’ll see:
```
On branch main
Your branch is up to date with 'origin/main'.
nothing to commit, working tree clean
```
To verify that your deployment is working, check your Railway logs:
Go to Railway → Deployments → Logs
Look for any error messages.

## 📝 Additional Resources

### Hire Developers:
 https://hng.tech/hire/python-developers
