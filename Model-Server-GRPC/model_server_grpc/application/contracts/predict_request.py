from dataclasses import dataclass
import pandas as pd


@dataclass
class PredictRequest:
    x: pd.DataFrame
    model_name: str