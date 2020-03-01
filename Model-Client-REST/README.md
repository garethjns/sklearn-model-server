# Model-Client-REST

Emulates a client by randomly requesting batch predictions from the REST model server. 

## Running service
Note that when running the server in a docker container, the paths returned to the client (whether running in docker or not) are to files in the server container. This obviously isn't ideal, but will be sorted when Min.io is added for shared storage.

### With docker:

Run:
````bash
docker build . -t model_client_rest
docker run model_client_rest
````

### With python:

(Optional) Set up environment. 
````bash
python3 -m venv envs/model_client_rest
source envs/model_client_rest/bin/activate
pip install .
````

Run:

````bash
python3 run.py
````
