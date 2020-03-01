# Model-Server-REST

Serves a model over HTTP with a Hug REST api. Receives requests containing the path to a .hdf file containing the data, saves the predictions to .csv, and returns the path to the predictions file.

## Request format
Predict requests should contain a path to a .hdf file and key containing a rows by features array only. 

eg.
````python
host = 'http://127.0.0.1'
port = '8000'
data_file = 'data/data_test.hdf'
data_key = 'test'
mod =  'SGDClassifier.pkl'

req = f"{host}:{port}/predict?mod={mod}&data_path={data_path}&data_key={data_key}
````

## Response format
Response is json containing a path to an output predictions file (.csv), eg.

Note that when running the server in a docker container, the paths returned to the client (whether running in docker or not) are to files in the server container. This obviously isn't ideal, but will be sorted when Min.io is added for shared storage. When running in python, the preds are dumped in the same folder as the original file..

````json
'{"pred_path": "data/data_test.hdf_client_16348_RandomForestClassifier.pkl_preds.csv"}'
````


## Training models
scripts/generate_data.py generates a small dataset using sklearn.datasets.make_classification.  
scripts/train_models.py trains an SGDClassifier and RandomForestClassifier models.  

The pre-generated and pre-trained models are included in data/ folder. The server loads the models from here. A copy of the data is also available to the Model-Client

When the Model-Trainer service is implemented, it will handle receiving data, training, and persisting to Min.io, which will replace the basic functionality here.


## Running service

### With docker:
````bash
sudo docker build . -t model_server_rest
sudo docker run -p 8000:8000 -t -i model_server_rest
````

### With Python:

(Optional) Set up environment
````bash
python3 -m venv envs/model_server_rest
source envs/model_server_rest/bin/activate
pip install .
````

Run:

````bash
./run.sh 
````


## Query service

The server can be accessed with curl, the module requests in Python, from a browser, etc. It returns json containing the location of the predictions output file in 'pred_path'eg.:
```json

```

### In browser
http://127.0.0.1:8000/predict?mod=SGDClassifier.pkl&data_path=data/data_test.hdf&data_key=test

### In python
````python
import requests
req = "http://127.0.0.1:8000/predict?mod=SGDClassifier.pkl&data_path=data/data_test.hdf&data_key=test"

response = requests.get(req)
````