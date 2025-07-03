import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from app.database import tweets_collection

nltk.download('stopwords')

def preprocess_tweet(text):
    text =re.sub(r'http\S+|www\S+|https\S+', '', text)
    text =re.sub(r'@\w+', '', text)
    text =re.sub(r'#[\w-]+', '', text)        
    text =re.sub(r'\d+', '', text)
    text =re.sub(r'[^\w\s]', '', text)    
    text = text.lower()
    return " ".join (word for word in text.split() if word not in stop_words.words('english'))


#  load  tweets csv
df = pd.read_csv('tweets.csv')
df = df[["text"]].dropna()
df["cleaned"] = df["text"].apply(clean_text)

# Insert cleaned tweets into MongoDB
tweets_collection.delete_many({})  
tweets_collection.insert_many(df.to_dict("records"))

print("Tweets inserted successfully!")
    