from dataclasses import dataclass
from model_server.application.contracts.predict_request import PredictRequest
from model_server_pb2 import GrpcPredictRequest, XRow
import pandas as pd


@dataclass
class PredictRequestMapper:
    def map(self, grpc_request: GrpcPredictRequest) -> PredictRequest:
        rows = []
        for x_i, x in enumerate(grpc_request.X):
            rows.append(pd.DataFrame({'f0': x.f0,
                                      'f1': x.f1,
                                      'f2': x.f2,
                                      'f3': x.f3,
                                      'f4': x.f4},
                                     index=[x_i]))

        return PredictRequest(x=pd.concat(rows,
                                          axis=0),
                              model_name=grpc_request.ModelName)
