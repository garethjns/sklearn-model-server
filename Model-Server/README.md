# Model-server

## Training models
scripts/generate_data.py generates a small dataset using sklearn.datasets.make_classification.  
scripts/train_models.py trains an ElasticNet and RandomForestClassifier models.  

The pre-generated and pre-trained models are included in data/ folder. The server loads the models from here. A copy of the data is also available to the Model-Client

When the Model-Trainer service is implemented, it will handle receiving data, training, and persisting to Minio, which will replace the basic functionality here.

## Preparing protos
This is only necessary after modifying proto definitions in protos/ (and Remember to update any clients too!)
 
Regenerate:
````bash
./generate.sh
````

## Running service

### With docker:
````bash
docker build . -t model_server
docker run -p 8080:8080 model_server
````

### With python:

(Optional) Set up environment
````bash
python3 -m venv envs/model_server
source envs/model_server/bin/activate
pip install .
````

Run:

````bash
python3 run.py
````
