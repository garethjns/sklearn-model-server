from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
import pandas as pd
import os


def generate_data(output_path: str = '.'):

    x, y = make_classification(n_samples=100000,
                               n_features=5,
                               n_informative=3,
                               flip_y=0.2)

    data = pd.DataFrame(x)
    data.columns = [f"f{n}" for n in data]
    data.loc[:, 'y'] = y

    train, test = train_test_split(data,
                                   train_size=0.25)

    train.to_hdf(os.path.join(output_path, 'data.hdf'),
                 mode='w',
                 key='train',
                 complevel=9)
    test.to_hdf(os.path.join(output_path, 'data.hdf'),
                mode='a',
                key='test',
                complevel=9)


if __name__ == "__main__":
    generate_data('../data/')
