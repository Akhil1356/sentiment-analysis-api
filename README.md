## Sentiment Analysis API (with Docker & Swagger) ##

A fully containerized microservice for sentiment analysis using VADER and FastAPI. 


 ## Prerequisites ##

- Python 3.10+
- Docker & Docker Compose



###  Docker Setup ##


# Step 1: Build the Docker images
docker-compose build

# Step 2: Run the containers
docker-compose up



 ## Test the API

Once the server is up, visit:

http://localhost:8000/docs
  




## Sample API Usage ##

✅ POST /analyze
json

Request:
{
  "text": "I love this product! It's awesome."
}

Response:
{
  "sentiment": "positive",
  "score": 0.6696
}

