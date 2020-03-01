import unittest

import pandas as pd

from model_server_rest.domain.model_predict import ModelPredict
from tests.common.fixtures.data_fixture import DataFixture
from tests.common.fixtures.model_fixture import ModelFixture


class TestModelPredict(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._data_fixture = DataFixture(data_dir='../../common/data/')
        cls._model_fixture = ModelFixture()
        cls._sut = ModelPredict(models_path=cls._model_fixture.model_path,
                                data_path=cls._data_fixture.data_path)

    def test_predict_batch(self):
        # Arrange
        x = self._data_fixture.load_data()
        mod = self._model_fixture.model_name

        # Act
        preds = self._sut.predict(x,
                                  model_name=mod)

        # Assert
        self.assertIsInstance(preds, pd.DataFrame)
