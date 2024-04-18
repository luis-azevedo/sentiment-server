import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.sentiment_analysis import SentimentAnalysis  # noqa: E501
from openapi_server import util


def sentiment_analysis(sentence=None):  # noqa: E501
    """Given a sentence it analyses whether the sentiment is positive or negative

    By passing in a sentence the service will return positive or negative.  # noqa: E501

    :param sentence: pass string with a sentence
    :type sentence: str

    :rtype: Union[SentimentAnalysis, Tuple[SentimentAnalysis, int], Tuple[SentimentAnalysis, int, Dict[str, str]]
    """
    return 'do some magic!'
