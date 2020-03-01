import time
from dataclasses import dataclass

import grpc
import numpy as np

from model_server_grpc.config import Config
from model_svc_pb2_grpc import ModelSvcStub
from tests.common.fixtures.data_fixture import DataFixture


@dataclass
class ModelClient:
    id = np.random.randint(1, 2 ** 16)
    _channel = grpc.insecure_channel(f'{Config().host}:{Config().port}')
    _stub = ModelSvcStub

    def query(self):
        stub = self._stub(self._channel)

        grpc_request = DataFixture().sample_rows_as_grpc_request(1)

        t0 = time.time()
        response = stub.predict(grpc_request)
        t1 = time.time()

        print(f"Client {self.id}: Returned prob: {response.Prob} in {np.round(t1 - t0, 2)}s")

    def continuous_chat(self):
        while True:
            time.sleep(np.abs(np.random.randn(1)) * 2)
            self.query()


if __name__ == "__main__":
    model_client = ModelClient()
    model_client.query()
    model_client.continuous_chat()
