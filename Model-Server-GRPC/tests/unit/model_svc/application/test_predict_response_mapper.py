import unittest

import pandas as pd

from model_server_grpc.application.predict_response_mapper import PredictResponseMapper
from model_server_grpc.application.contracts.predict_response import PredictResponse


class TestPredictRequestMapper(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._sut = PredictResponseMapper()

    def test_map(self):
        response = PredictResponse(prob=0.5)

        grpc_response = self._sut.map(response)

        self.assertEqual(grpc_response.Prob, response.prob)
