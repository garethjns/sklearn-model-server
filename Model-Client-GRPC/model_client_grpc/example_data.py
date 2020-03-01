import os
from dataclasses import dataclass

import numpy as np
import pandas as pd

from model_svc_pb2 import GrpcPredictRequest, XRow


@dataclass
class ExampleData:
    path: str = 'data/'
    fn: str = 'data.hdf'
    data: pd.DataFrame = None

    def __post_init__(self):
        self.get_data()

    def get_data(self):
        if self.data is None:
            os.sep = '/'
            path = os.path.join(os.getcwd(), self.path).replace('\\', '/')

            self.data = pd.read_hdf(os.path.join(path, self.fn),
                                    key='test')

    def sample_rows(self, n: int) -> pd.DataFrame:
        return self.data.loc[self.data.index[np.random.randint(0, self.data.shape[0], n)],
                             [c for c in self.data if c != 'y']]

    def sample_rows_as_grpc_request(self, n: int, **kwargs) -> GrpcPredictRequest:
        x = self.sample_rows(n)

        return GrpcPredictRequest(ModelName=np.random.choice(['SGDClassifier.pkl', 'RandomForestClassifier.pkl']),
                                  X=[XRow(f0=r.f0, f1=r.f1, f2=r.f2, f3=r.f3, f4=r.f4)
                                     for r_i, r in x.iterrows()],
                                  **kwargs)
