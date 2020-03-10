import json
import sys
import threading
import time
import unittest

import requests

from model_server_rest.application.model_endpoint import ModelEndpoint
from tests.common.fixtures.data_fixture import DataFixture
from tests.common.model_server import ModelServer
from tests.config import Config
import os


valid_env = os.environ.get('RUN_MODEL_SERVER_REST_INTEGRATION_TESTS', False) is not False


@unittest.skipUnless(valid_env, "Skipping test in CI/Windows")
class TestModelEndpoint(unittest.TestCase):
    _sut = ModelEndpoint()
    _test_server: threading.Thread
    _data_fixture = DataFixture()
    _config = Config()

    @classmethod
    def setUpClass(cls) -> None:
        cls._test_server = threading.Thread(target=ModelServer().start_server)
        cls._test_server.daemon = True
        cls._test_server.start()
        time.sleep(2)

    def test_response_received_from_test_data_request(self):
        # Arrange
        request = self._data_fixture.build_rest_request(host=self._config.test_host,
                                                        port=self._config.test_port)

        # act - uses sut, but via hug
        response = requests.get(request)

        # assert
        response_message = json.loads(response.text)
        self.assertEqual(200, response.status_code)
        self.assertIsInstance(response_message, dict)
        self.assertIsInstance(response_message['preds_path'], str)

    @classmethod
    def tearDownClass(cls) -> None:
        sys.exit()
