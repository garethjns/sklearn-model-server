import json
import time
from dataclasses import dataclass

import numpy as np
import requests

from model_server_rest.config import Config
from tests.common.fixtures.data_fixture import DataFixture


@dataclass
class ModelClient:
    id = np.random.randint(1, 2 ** 16)

    def query(self, request: str):
        t0 = time.time()
        response = requests.get(request)
        t1 = time.time()

        print(f"Client {self.id}: Returned path: {json.loads(response.text)['preds_path']} in {np.round(t1 - t0, 2)}s")

    def continuous_chat(self, request: str):
        while True:
            time.sleep(np.abs(np.random.randn(1)) * 2)
            self.query(request)


if __name__ == "__main__":
    data_fixture = DataFixture()
    model_client = ModelClient()
    request_ = data_fixture.build_rest_request(host=Config().host,
                                               port=Config().port)
    model_client.query(request_)
    model_client.continuous_chat(request_)
