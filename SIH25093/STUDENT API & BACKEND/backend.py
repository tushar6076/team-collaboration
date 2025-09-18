from flask import Flask, render_template_string
import requests

app = Flask(__name__)
API_URL = "http://127.0.0.1:8000"

@app.route('/')
def index():
    try:
        response = requests.get(f"{API_URL}/data")
        response.raise_for_status()
        data = response.json()
        message = data.get("message", "API connection failed")
    except requests.exceptions.RequestException:
        message = "Could not connect to FastAPI server."
    
    return render_template_string(f"""
        <!doctype html>
        <title>Flask Web App</title>
        <h1>Message from FastAPI:</h1>
        <p>{message}</p>
    """)

if __name__ == "__main__":
    # Ensure the FastAPI backend is running first
    app.run(port=5000)