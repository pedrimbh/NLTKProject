from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_sentiment_analysis():
    response = client.post("/sentiment-analysis", json={"text": "I love my life"})
    assert response.status_code == 200
    assert response.json() == {'result': {'compound': 0.6369, 'neg': 0.0, 'neu': 0.323, 'pos': 0.677}}


def test_tokenize():
    response = client.post("/tokenizer", json={"text": "I love my life"})
    assert response.status_code == 200
    assert response.json() == {'tokens': ['I', 'love', 'my', 'life']}
