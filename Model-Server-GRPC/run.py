from model_server_grpc.model_server import ModelServer


if __name__ == "__main__":
    model_server = ModelServer()
    model_server.start_server(block=True)
