import pandas as pd


def create_example_test_hdf():

    data = pd.read_hdf('../data/data.hdf',
                       key='test')[['f0', 'f1', 'f2', 'f3', 'f4']]

    data.to_hdf('../data/data_test.hdf',
                key='test')


if __name__ == "__main__":
    create_example_test_hdf()
