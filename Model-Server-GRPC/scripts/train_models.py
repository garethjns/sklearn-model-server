import os
import pickle
from typing import Callable, Dict, Iterable, Any

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import RandomizedSearchCV
from IPython.display import display


COMMON_GRID_PARAMS = {'n_iter': 40,
                      'n_jobs': -2,
                      'verbose': 1,
                      'scoring': 'roc_auc',
                      'return_train_score': True,
                      'refit': False}

RFC_GRID = {'n_estimators': [20],
            'min_samples_split': [4, 8, 16, 32, 64, 128],
            'min_samples_leaf': [4, 8, 16, 32, 64, 128],
            'max_features': ['log2', 'sqrt', 0.2, 0.4]}

SGD_GRID = {'loss': ['log'],
            'alpha': [0.01, 0.1, 1, 10],
            'penalty': ['elasticnet'],
            'l1_ratio': [0, 0.25, 0.5, 0.75, 1],
            'fit_intercept': [True, False]}


def train_models(output_path: str = '.'):
    train = pd.read_hdf("../data/data.hdf",
                        key="train")

    for model, grid_params in zip([RandomForestClassifier, SGDClassifier], [RFC_GRID, SGD_GRID]):
        mod = train_model(train[[c for c in train if c != 'y']], train.y, model, grid_params)

        pickle.dump(mod, open(os.path.join(output_path, f"{model.__name__}.pkl"), 'wb'))


def train_model(x: np.ndarray, y: np.ndarray, model: Callable, grid_params: Dict[str, Iterable[Any]]):
    grid = RandomizedSearchCV(model(),
                              param_distributions=grid_params,
                              **COMMON_GRID_PARAMS)

    grid.fit(x, y)
    display(pd.DataFrame(grid.cv_results_).sort_values('mean_test_score',
                                                       ascending=False)[['mean_train_score',
                                                                         'mean_test_score']].head(20))

    mod = model(**grid.best_params_)
    mod.fit(x, y)

    return mod


if __name__ == "__main__":
    train_models(output_path='../data/models/')