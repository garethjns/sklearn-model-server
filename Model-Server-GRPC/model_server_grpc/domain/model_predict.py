import glob
import os
import pickle
from dataclasses import dataclass
from typing import Dict

import sklearn

from model_server_grpc.application.contracts.predict_request import PredictRequest
from model_server_grpc.application.contracts.predict_response import PredictResponse
from model_svc_grpc import ModelServerBase


@dataclass
class ModelPredict(ModelServerBase):
    models_path: str = 'data/models/'
    models: Dict[str, sklearn.base.BaseEstimator] = None

    def __post_init__(self):
        self._load_models()

    def _load_models(self):
        self.models = {}
        mod_paths = glob.glob(os.path.join(self.models_path, '*.pkl'))

        for mod_path in mod_paths:
            mod_name = mod_path.replace('\\', '/').split('/')[-1]
            self.models[mod_name] = pickle.load(open(mod_path, 'rb'))

    def predict(self, request: PredictRequest) -> PredictResponse:
        return PredictResponse(prob=self.models[request.model_name].predict_proba(request.x)[:, 0])
