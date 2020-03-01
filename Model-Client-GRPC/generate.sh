#!/bin/bash
python -m grpc_tools.protoc -I protos --python_out=. --python_grpc_out=. protos/model_server.proto