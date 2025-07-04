import pandas as pd
from app.database import tweets_collection
from app.utils import clean_text

# Load your tweet dataset
df = pd.read_csv("tweets.csv")


df = df[["text"]].dropna()


df["cleaned"] = df["text"].apply(clean_text)

# Convert to list of dictionaries for MongoDB insertion
records = df.to_dict("records")

# Insert into MongoDB
tweets_collection.delete_many({})  
tweets_collection.insert_many(records)

print("Cleaned tweets inserted into MongoDB.")
