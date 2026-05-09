# SHL AI Conversational Assessment Recommender

An AI-powered conversational recommendation system for SHL assessments built using FastAPI, Gemini AI, and intelligent retrieval logic.

## Features

- Conversational assessment recommendation
- SHL catalog-based recommendations
- Clarification handling
- Refinement support
- Comparison support
- Off-topic refusal
- FastAPI REST API
- Gemini AI integration
- Public deployment on Render

## Tech Stack

- FastAPI
- Python
- Gemini AI
- BeautifulSoup
- Render
- JSON-based retrieval

## API Endpoints

### Health Check

GET /health

Response:

```json
{
  "status": "ok"
}
```

### Chat Endpoint

POST /chat

Request:

```json
{
  "messages": [
    {
      "role": "user",
      "content": "Hiring Java developer with communication skills"
    }
  ]
}
```

## Deployment

Live URL:

https://shl-ai-recommender-n0uq.onrender.com

## Run Locally

```bash
pip install -r requirements.txt
uvicorn app:app --reload
```

## Author

Agrasen Patel