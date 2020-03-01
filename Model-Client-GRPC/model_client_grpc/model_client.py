import asyncio
import time
from dataclasses import dataclass

import numpy as np
from grpclib.client import Channel

from model_client_grpc.config import Config
from model_client_grpc.example_data import ExampleData
from model_svc_grpc import ModelServerStub


@dataclass
class ModelClient:
    id = np.random.randint(1, 2 ** 16)
    _channel = Channel(Config().host, Config().port)
    _stub = ModelServerStub

    def query(self,
              close_loop: bool = True):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self._query())

        if close_loop:
            loop.close()
        else:
            return loop

    async def _query(self):
        stub = self._stub(self._channel)

        grpc_request = ExampleData().sample_rows_as_grpc_request(1, ClientId=self.id)

        print(grpc_request)

        t0 = time.time()
        response = await stub.predict(grpc_request)
        t1 = time.time()

        print(f"Client {self.id}: Returned prob: {response.Prob} in {np.round(t1 - t0, 2)}s")

    def continuous_chat(self):
        while True:
            try:
                time.sleep(np.abs(np.random.randn(1)) * 5)
                loop = self.query(close_loop=False)
            except ConnectionRefusedError:
                pass
            except KeyboardInterrupt:
                loop.close()


if __name__ == "__main__":
    model_client = ModelClient()
    model_client.query()
    model_client.continuous_chat()
