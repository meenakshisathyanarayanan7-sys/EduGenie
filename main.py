from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field
from dotenv import load_dotenv
load_dotenv()

from qna import answer_question
from explanation_module import explain_concept
from quiz_module import generate_quiz
from summary_module import summarize_text
from learning_path import get_learning_recommendations


# Load environment variables
load_dotenv()

# Project directory
BASE_DIR = Path(__file__).resolve().parent

# Create FastAPI application
app = FastAPI(
    title="EduGenie",
    description="Google Gemini Powered Learning Assistant",
    version="1.0.0"
)

# Static files
app.mount(
    "/static",
    StaticFiles(directory=BASE_DIR / "static"),
    name="static"
)

# HTML templates
templates = Jinja2Templates(
    directory=str(BASE_DIR / "templates")
)


# Request model
class TextRequest(BaseModel):
    text: str = Field(
        ...,
        min_length=1,
        max_length=20000
    )


# Home page
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"request": request},
    )
    


# Health check
@app.get("/health")
async def health():
    return {
        "status": "ok",
        "service": "EduGenie"
    }


# Question and Answer
@app.post("/qa")
async def qa(request: TextRequest):

    result = answer_question(request.text)

    return {
        "result": result
    }


# Explain concept
@app.post("/explain")
async def explain(request: TextRequest):

    result = explain_concept(request.text)

    return {
        "result": result
    }


# Generate quiz
@app.post("/quiz")
async def quiz(request: TextRequest):

    result = generate_quiz(request.text)

    return {
        "result": result
    }


# Summarize text
@app.post("/summarize")
async def summarize(request: TextRequest):

    result = summarize_text(request.text)

    return {
        "result": result
    }


# Learning recommendations
@app.post("/learn/recommendations")
async def recommendations(request: TextRequest):

    result = get_learning_recommendations(request.text)

    return {
        "result": result
    }