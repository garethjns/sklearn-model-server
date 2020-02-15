import time

import numpy as np

from model_server.application.predict_request_mapper import PredictRequestMapper
from model_server.application.predict_response_mapper import PredictResponseMapper
from model_server.domain.model_predict import ModelPredict
from model_server_grpc import ModelServerBase


class ModelEndpoint(ModelServerBase):
    _model_predict = ModelPredict()
    _predict_request_mapper = PredictRequestMapper()
    _predict_response_mapper = PredictResponseMapper()

    async def predict(self, stream):
        t0 = time.time()

        grpc_request = await stream.recv_message()
        request = self._predict_request_mapper.map(grpc_request)

        response = self._model_predict.predict(request)

        grpc_response = self._predict_response_mapper.map(response)

        await stream.send_message(grpc_response)

        t1 = time.time()
        print(f"Responded to a request from {getattr(grpc_request, 'ClientId', 'unknown')} for {grpc_request.ModelName}"
              f" in {np.round(t1 - t0, 2)}s")


if __name__ == "__main__":
    model_endpoint = ModelEndpoint()
