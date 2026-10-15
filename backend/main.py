import os
import json
from dotenv import load_dotenv, find_dotenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from google import genai
from google.genai import types

load_dotenv(find_dotenv())
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

MODEL = "gemini-3.5-flash-lite"

app = FastAPI(title="AI Study Buddy")


def ask_json(prompt: str) -> dict:
    """Gemini ku prompt anuppi JSON ah thirumba tharum helper."""
    try:
        r = client.models.generate_content(
            model=MODEL,
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json"
            ),
        )
        return json.loads(r.text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/")
def health():
    return {"status": "ok"}


class QuizRequest(BaseModel):
    topic: str
    notes: str = ""
    num_questions: int = Field(5, ge=1, le=10)


@app.post("/quiz")
def generate_quiz(req: QuizRequest):
    source = req.notes if req.notes else f"General knowledge about {req.topic}"
    prompt = f"""Create {req.num_questions} multiple choice questions on "{req.topic}"
based on this content:

{source}

Return ONLY JSON in this format:
{{"questions": [
  {{"question": "...",
    "options": ["A", "B", "C", "D"],
    "answer_index": 0,
    "explanation": "..."}}
]}}"""
    return ask_json(prompt)


class SummarizeRequest(BaseModel):
    text: str


@app.post("/summarize")
def summarize(req: SummarizeRequest):
    prompt = f"""Summarize the following study notes for a student.

{req.text}

Return ONLY JSON in this format:
{{"summary": "short paragraph",
  "key_points": ["point 1", "point 2", "point 3"]}}"""
    return ask_json(prompt)


class FlashcardRequest(BaseModel):
    topic: str
    notes: str = ""
    num_cards: int = Field(5, ge=1, le=15)


@app.post("/flashcards")
def flashcards(req: FlashcardRequest):
    source = req.notes if req.notes else f"General knowledge about {req.topic}"
    prompt = f"""Create {req.num_cards} flashcards on "{req.topic}"
based on this content:

{source}

Return ONLY JSON in this format:
{{"cards": [{{"front": "question or term", "back": "answer or definition"}}]}}"""
    return ask_json(prompt)