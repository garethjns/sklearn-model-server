import unittest

import pandas as pd

from model_server.application.predict_request_mapper import PredictRequestMapper
from tests.common.fixtures.data_fixture import DataFixture


class TestPredictRequestMapper(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._data_fixture = DataFixture()
        cls._sut = PredictRequestMapper()

    def test_map(self):
        grpc_request = self._data_fixture.sample_rows_as_grpc_request(1)

        request = self._sut.map(grpc_request)

        self.assertEqual(request.model_name, 'SGDClassifier.pkl')
        self.assertIsInstance(request.x, pd.DataFrame)
