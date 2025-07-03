from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from pymongo import MongoClient
from typing import List
import io

app = FastAPI()

# MongoDB setup
client = MongoClient("mongodb://mongodb:27017/")
db = client["sentiment_db"]
collection = db["tweets"]

# VADER Sentiment Analyzer
analyzer = SentimentIntensityAnalyzer()

# Endpoint 1: Upload and analyze CSV
@app.post("/upload_csv")
async def upload_csv(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        df = pd.read_csv(io.StringIO(contents.decode("utf-8")))

        if "text" not in df.columns:
            return JSONResponse(status_code=400, content={"error": "CSV must contain a 'text' column."})

        result = []
        for text in df["text"]:
            sentiment_score = analyzer.polarity_scores(str(text))["compound"]
            sentiment = (
                "positive" if sentiment_score >= 0.05 else
                "negative" if sentiment_score <= -0.05 else
                "neutral"
            )
            result.append({"text": text, "sentiment": sentiment, "score": sentiment_score})

        collection.insert_many(result)
        return {"message": f"{len(result)} tweets processed and stored in MongoDB."}

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

# Endpoint 2: Analyze a single text
class SentimentRequest(BaseModel):
    text: str

@app.post("/analyze")
def analyze_sentiment(data: SentimentRequest):
    scores = analyzer.polarity_scores(data.text)
    sentiment = (
        "positive" if scores["compound"] >= 0.05 else
        "negative" if scores["compound"] <= -0.05 else
        "neutral"
    )
    return {
        "text": data.text,
        "sentiment": sentiment,
        "score": scores["compound"]
    }

# Optional root endpoint
@app.get("/")
def root():
    return {"message": "Sentiment Analysis API is running."}
