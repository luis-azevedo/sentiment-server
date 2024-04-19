import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.sentiment_analysis import SentimentAnalysis  # noqa: E501
from openapi_server import util

# Import sentiment analysis models
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer


def sentiment_analysis(sentence=None):  # noqa: E501
    """Given a sentence it analyses whether the sentiment is positive or negative

    By passing in a sentence the service will return positive or negative.  # noqa: E501

    :param sentence: pass string with a sentence
    :type sentence: str

    :rtype: Union[SentimentAnalysis, Tuple[SentimentAnalysis, int], Tuple[SentimentAnalysis, int, Dict[str, str]]
    """
    # Analyse the  supplied query
    sentiment_computed =''
    nltk.download("vader_lexicon")
    sid = SentimentIntensityAnalyzer()
    score = sid.polarity_scores(sentence)["compound"]
    if score > 0:
        sentiment_computed = 'positive' # if score is greater than zero return positive
    else:
        sentiment_computed =  'negative' # if score is greater than zero return negative     

    senti = SentimentAnalysis(
        sentiment = sentiment_computed
    )
    return senti

