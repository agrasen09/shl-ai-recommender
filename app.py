from fastapi import FastAPI
from pydantic import BaseModel
from chatbot import chatbot_response

app = FastAPI()

# Request schema
class ChatRequest(BaseModel):
    messages: list

@app.get("/")
def home():
    return {
        "message": "SHL AI Assessment Recommender Running"
    }

@app.get("/health")
def health():
    return {
        "status": "ok"
    }

@app.post("/chat")
def chat(request: ChatRequest):

    response = chatbot_response(request.messages)

    return response