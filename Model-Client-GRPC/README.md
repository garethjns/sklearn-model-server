# Model-Client-GRPC

Emulates a client by randomly requesting predictions from the GRPC model server.

## Running service

### With docker:

Run:
````bash
sudo docker build . -t model_client_grpc
sudo docker run model_client_grpc
````

### With python:

(Optional) Set up environment. 
````bash
python3 -m venv envs/model_client_grpc
source envs/model_client_grpc/bin/activate
pip install .
````

Run:

````bash
python3 run.py
````
