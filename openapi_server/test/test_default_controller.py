import unittest

from flask import json

from openapi_server.models.sentiment_analysis import SentimentAnalysis  # noqa: E501
from openapi_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_sentiment_analysis(self):
        """Test case for sentiment_analysis

        Given a sentence it analyses whether the sentiment is positive or negative
        """
        query_string = [('sentence', 'The day is beautiful')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/sentiment',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
