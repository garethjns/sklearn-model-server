import glob
import os
import pickle
from dataclasses import dataclass
from typing import Dict, Union

import numpy as np
import pandas as pd
import sklearn


@dataclass
class ModelPredict:
    client_id: str = 'default_client'
    models_path: str = 'data/models/'
    data_path: str = 'data/data.hdf'
    models: Dict[str, sklearn.base.BaseEstimator] = None

    def __post_init__(self):
        self._load_models()

    def _load_models(self):
        self.models = {}
        mod_paths = glob.glob(os.path.join(self.models_path, '*.pkl'))

        for mod_path in mod_paths:
            mod_name = mod_path.replace('\\', '/').split('/')[-1]
            self.models[mod_name] = pickle.load(open(mod_path, 'rb'))

    @staticmethod
    def load_data(data_path: str, key: str) -> pd.DataFrame:
        return pd.read_hdf(data_path,
                           key=key)

    def save_data(self, preds: np.array, mod: str, data_path: str) -> str:
        preds_path = f"{data_path.split('.csv')[0]}_client_{self.client_id}_{mod}_preds.csv"
        pd.DataFrame(preds).to_csv(preds_path)

        return preds_path

    def predict(self, x: Union[np.array, pd.DataFrame], model_name: str) -> np.array:
        return self.models[model_name].predict_proba(x)[:, 0]
