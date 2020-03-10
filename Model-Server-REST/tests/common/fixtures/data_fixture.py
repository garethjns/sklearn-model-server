import os
from dataclasses import dataclass

import pandas as pd
from tests.common.fixtures.sample_data import SAMPLE_DATA


@dataclass
class DataFixture:
    data_dir: str = 'tests/common/data/'
    data_fn: str = 'data_test.hdf'
    data_key = 'test'

    def __post_init__(self):
        self._set_data_path()

    def _set_data_path(self):
        os.sep = '/'
        path = os.path.join(self.data_dir, self.data_fn).replace('\\', '/')

        self.data_path = path

    def load_data(self) -> pd.DataFrame:
        try:
            return pd.read_hdf(self.data_path,
                               key=self.data_key)
        except FileNotFoundError:
            return pd.DataFrame(SAMPLE_DATA)[["f0", "f1", "f2", "f3", "f4"]]

    def build_rest_request(self, host: str, port: str) -> str:
        model_name = 'SGDClassifier.pkl'
        return f"http://{host}:{port}/predict?mod={model_name}&data_path={self.data_path}&data_key=test"
