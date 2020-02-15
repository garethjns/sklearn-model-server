from dataclasses import dataclass

import numpy as np


@dataclass
class PredictResponse:
    prob: np.ndarray
