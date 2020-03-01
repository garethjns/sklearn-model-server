import json
import time
from dataclasses import dataclass

import numpy as np
import requests

from model_client_rest.config import Config


@dataclass
class ModelClient:
    id = np.random.randint(1, 2 ** 16)
    _config = Config()

    def _build_request(self, data_path: str,
                       model_name: str) -> str:
        return f"http://{self._config.host}:{self._config.port}/predict?&client_id={self.id}&mod={model_name}&data_path={data_path}&data_key=test"

    def query(self, data_path: str,
              model_name: str = 'SGDClassifier.pkl'):

        request = self._build_request(data_path, model_name)

        t0 = time.time()
        response = requests.get(request)
        t1 = time.time()

        print(f"Client {self.id}: Returned path: {json.loads(response.text)['preds_path']} in {np.round(t1 - t0, 2)}s")

    def continuous_chat(self, data_path: str,
                        model_name: str = 'SGDClassifier.pkl'):
        while True:
            time.sleep(np.abs(np.random.randn(1)) * 5)
            self.query(data_path,
                       model_name=np.random.choice(['SGDClassifier.pkl', 'RandomForestClassifier.pkl']))


if __name__ == "__main__":
    model_client = ModelClient()
    model_client.query(data_path='../data/data_test.hdf')
    model_client.continuous_chat(data_path='../data/data_test.hdf')
