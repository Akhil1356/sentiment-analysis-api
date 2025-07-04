from fastapi import FastAPI
from app.database import tweets_collection
from app.sentiment import analyze_sentiment

app = FastAPI()

#  API 1: GET /get-tweets 
@app.get("/get-tweets")
def get_cleaned_tweets(limit: int = 10):
    tweets = list(tweets_collection.find({}, {"_id": 0, "cleaned": 1}))
    return {"tweets": tweets[:limit]}

#  API 2: POST /analyze-sentiment 
@app.post("/analyze-sentiment")
def analyze_cleaned_tweets():
    tweets = list(tweets_collection.find({}, {"_id": 0, "cleaned": 1}))
    analyzed = []

    for tweet in tweets:
        cleaned_text = tweet.get("cleaned", "")
        sentiment = analyze_sentiment(cleaned_text)
        analyzed.append({
            "cleaned": cleaned_text,
            "sentiment": sentiment
        })

    return {"results": analyzed}
