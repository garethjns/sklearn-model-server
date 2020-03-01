from model_client_rest.model_client import ModelClient


def run_client(data_path: str):
    model_client = ModelClient()
    model_client.query(data_path=data_path)
    model_client.continuous_chat(data_path=data_path)


if __name__ == "__main__":
    run_client('data/data_test.hdf')
