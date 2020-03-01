import os
import subprocess

from model_server_rest.application.model_endpoint import ModelEndpoint


class ModelServer:
    _endpoint = ModelEndpoint()

    @staticmethod
    def start_server():
        # Handle possibility of running in tests subdirectory
        path = os.getcwd().split('/tests')[0]
        os.chdir(path)
        subprocess.call(os.path.join(path, "run.sh"))


if __name__ == "__main__":
    ModelServer().start_server()
