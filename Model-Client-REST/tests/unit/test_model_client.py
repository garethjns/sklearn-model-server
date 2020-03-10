import unittest

from model_client_rest.model_client import ModelClient


class TestModelClient(unittest.TestCase):
    _sut = ModelClient()

    def test_model_client_init(self):
        """This is really just to have a test so pytest doesn't get upset."""
        self.assertIsInstance(self._sut, ModelClient)
