from fastapi import APIRouter, HTTPException, status, Path, Body
from Models.InputModel import InputModel
from MLModels.SentimentAnalysisMLModel import sentiment_analysis

router = APIRouter()


@router.post("/sentiment-analysis", tags=["Sentiment Analysis"],summary="Retorna a analise de sentimento baseado no texto inserido, aceita somente textos em Ingles",response_model=InputModel)
async def analyze_sentiment(input_data: InputModel):
    """
    Analisa o sentimento de um texto fornecido, aceita somente frases em Ingles.

    Args:
        input_data (InputModel): O modelo de entrada contendo o texto a ser analisado.

    Returns:
         dict: Um dicionário contendo a pontuação de sentimento calculada. A pontuação inclui valores
               para 'neg' (negativo), 'neu' (neutro), 'pos' (positivo) e 'compound' (composto).

    Raises:
        HTTPException: Se o texto fornecido estiver vazio.
    """
    try:
        if not input_data.text:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="O texto não pode ser vazio. Por favor, insira algum texto."
            )

        sentiment_score = sentiment_analysis(input_data.text)
        return {"result": sentiment_score}

    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
