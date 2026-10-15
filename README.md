# AI Study Buddy 📚

An AI-powered study assistant that helps students learn faster using Google Gemini.

## Features
- 💬 **Tutor Chat**: explains concepts simply, with modes (Simple, Explain like I'm 5, Exam-focused, Tamil + English)
- 📝 **Summarizer**: turns long notes into key points
- ❓ **Quiz Generator**: MCQs with difficulty levels, instant feedback and score
- 🃏 **Flashcards**: flip cards for quick revision
- 🗓 **Study Planner**: day-by-day plan based on your goal and time
- ⏱ **Pomodoro Timer**: focus and break sessions
- 📈 **Progress Tracker**: quiz score history and average

## Tech Stack
- Backend: Python, FastAPI
- AI: Google Gemini API
- Frontend: HTML, CSS, JavaScript

## Project Structure
```
AI-STUDY-BUDDY/
├── backend/      # FastAPI backend (quiz, summarize, flashcards, tutor chat)
├── frontend/     # index.html (web app)
├── .env.example
└── requirements.txt
```

## How to Run

### Frontend
1. Open `frontend/index.html` in your browser.
2. Paste your Gemini API key in the top-right box.
3. Start learning!

### Backend
1. Install dependencies: `pip install -r requirements.txt`
2. Copy `.env.example` to `.env` and add your key: `GEMINI_API_KEY=your_key_here`
3. Run: `cd backend` then `uvicorn main:app --reload`
4. Open `http://127.0.0.1:8000/docs` to test the API.

Get a free Gemini API key at https://aistudio.google.com/apikey

## Team
- JAISRI D: Knowledge base and tutor chat
- Jeevitha A: Quiz, summarizer and flashcards
- Ishwarya S: Frontend, demo and documentation
