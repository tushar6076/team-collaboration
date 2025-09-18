from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

# In-memory database to simulate data storage
db = {"message": "Hello from FastAPI!"}

class Message(BaseModel):
    message: str

@app.get("/data")
def get_message():
    """Endpoint for Kivy and Flask to get data."""
    return db

@app.post("/data")
def post_message(new_message: Message):
    """Endpoint for Kivy to post data."""
    db["message"] = new_message.message
    return {"status": "success", "message": "Updated"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)