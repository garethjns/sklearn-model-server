import os
from dataclasses import dataclass

import numpy as np
import pandas as pd


@dataclass
class ModelFixture:
    path: str = 'tests/common/data/models/'
    fn: str = 'SGDClassifier.pkl'

    @property
    def model_path(self) -> str:
        path = os.path.join(os.getcwd(), self.path).replace('\\', '/')
        if not os.path.exists(path):
            path = os.path.join(os.getcwd(), '../..', self.path).replace('\\', '/')

        return path

    @property
    def model_name(self) -> str:
        return self.fn

