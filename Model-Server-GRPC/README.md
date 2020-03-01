# Model-Server-GRPC

Serves a model over RPC. Receives prediction requests containing the full data, and returns an array of probabilities.

## Request format
Note the pre-trained models expect 5 numeric features - see "training models" section below.

```proto
message XRow {
    float f0 = 1;
    float f1 = 2;
    float f2 = 3;
    float f3 = 4;
    float f4 = 5;
}

message GrpcPredictRequest {
    int32 ClientId = 1;
    repeated XRow X = 2;
    string ModelName = 3;
}
```

## Response format
```proto
message GrpcPredictResponse {
    repeated float Prob = 1;
}
```


## Training models
scripts/generate_data.py generates a small dataset using sklearn.datasets.make_classification.  
scripts/train_models.py trains an SGDClassifier and RandomForestClassifier models.  

The pre-generated and pre-trained models are included in data/ folder. The server loads the models from here. A copy of the data is also available to the Model-Clients

When the Model-Trainer service is implemented, it will handle receiving data, training, and persisting to Min.io, which will replace the basic functionality here.

## Preparing protos
This is only necessary after modifying proto definitions in protos/ (and Remember to update any clients too!)
 
Regenerate:
````bash
./generate.sh
````

## Running service

### With docker:
````bash
sudo docker build . -t model_server_grpc
sudo docker run -p 8080:8080 model_server_grpc
````

### With python:

(Optional) Set up environment
````bash
python3 -m venv envs/model_server_grpc
source envs/model_server_grpc/bin/activate
pip install .
````

Run:

````bash
python3 run.py
````
