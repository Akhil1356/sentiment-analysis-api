## Sentiment Analysis API (Microservice) ##

This project is an end-to-end microservice-based sentiment analysis system built with **FastAPI**, **MongoDB**, and **VADER Sentiment Analyzer**. It allows you to:

- Upload and clean tweet data
- Store it in MongoDB
- Analyze tweet sentiments using VADER
- Run everything using Docker


 ## Prerequisites ##

- Python 3.10+
- Docker & Docker Compose

### 1. Clone the Repo


   git clone https://github.com/Akhil1356/sentiment-analysis-api.git
   
   cd sentiment-analysis-api



## Build and Run with Docker ##

docker-compose up --build -d

This will:

Build the FastAPI container

Spin up MongoDB container

Run the app at: http://localhost:8000


 ## Insert Cleaned Tweets into MongoDB
Once containers are running, enter the API container:


      docker exec -it sentiment_analysis-api-1 bash


 ## Inside the container, run:


    PYTHONPATH=/code python app/loader.py  

     ## Cleaned tweets inserted into MongoDB.    

 ## API Endpoints (Swagger UI)

Visit: http://localhost:8000/docs



