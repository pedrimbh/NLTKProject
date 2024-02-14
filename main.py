from fastapi import FastAPI

from Routes.SentimentAnalysisRoute import router as sentiment_analysis_router
from Routes.TokenizeRoute import router as token_router
from Config.Config import Config

Config()
app = FastAPI(title="API NLTK Blip Teste", description="API que faz o uso da biblioteca NLTK", version="0.1.0")

app.include_router(router=sentiment_analysis_router)
app.include_router(router=token_router)
