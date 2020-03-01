import unittest

from model_server_grpc.domain.model_predict import ModelPredict
from tests.common.fixtures.data_fixture import DataFixture
from tests.common.fixtures.model_fixture import ModelFixture


class TestModelPredict(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data_fixture = DataFixture()
        cls.model_fixture = ModelFixture()
        cls.model_predict = ModelPredict(models_path=cls.model_fixture.model_path)

    def test_predict_with_single_row(self):
        # Arrange
        request = self.data_fixture.sample_rows_as_request(1)

        # Act
        response = self.model_predict.predict(request)
        # Assert
        self.assertEqual(len(response.prob), 1)

    def test_predict_batch(self):
        # Arrange
        request = self.data_fixture.sample_rows_as_request(10)

        # Act
        response = self.model_predict.predict(request)
        # Assert
        self.assertEqual(len(response.prob), 10)
