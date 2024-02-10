from Models.InputModel import InputModel
from nltk.sentiment import SentimentIntensityAnalyzer


def sentiment_analysis(input: InputModel):
    """
     Realiza análise de sentimento em um texto usando a biblioteca NLTK.

     Args:
         input (InputModel): O objeto de entrada contendo o texto a ser analisado.

     Returns:
         dict: Um dicionário contendo a pontuação de sentimento calculada. A pontuação inclui valores
               para 'neg' (negativo), 'neu' (neutro), 'pos' (positivo) e 'compound' (composto).
     """
    sia = SentimentIntensityAnalyzer()
    sentiment_score = sia.polarity_scores(input)
    return sentiment_score


