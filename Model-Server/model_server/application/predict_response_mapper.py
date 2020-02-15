from dataclasses import dataclass

from model_server_pb2 import GrpcPredictResponse


@dataclass
class PredictResponseMapper:
    def map(self, response) -> GrpcPredictResponse:
        return GrpcPredictResponse(Prob=response.prob)
