# Sklearn-Model-Servers

![Test Model-Client-GRPC](https://github.com/garethjns/sklearn-model-server/workflows/Test%20Model-Client-GRPC/badge.svg)
![Test Model-Client-REST](https://github.com/garethjns/sklearn-model-server/workflows/Test%20Model-Client-REST/badge.svg)
![Test Model-Server-GRPC](https://github.com/garethjns/sklearn-model-server/workflows/Test%20Model-Server-GRPC/badge.svg)
![Test Model-Server-REST](https://github.com/garethjns/sklearn-model-server/workflows/Test%20Model-Server-REST/badge.svg)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=garethjns_sklearn-model-server&metric=alert_status)](https://sonarcloud.io/dashboard?id=garethjns_sklearn-model-server)

A small set of Dockerized microservices for training and serving Sklearn models over gRPC and REST. Currently includes a server and a client that hassles the server for predictions. 

The servers include pre-trained models on generated data. These are handled locally, but in the future the training will be moved to a separate service, and models and data will be persisted in a will be moved to a Minio instance. 


 ## Running
 Running the whole system requires docker and docker-compose, running the individual services just requires docker.
 
 ### Docker-compose

 ```bash
sudo docker-compose build
sudo docker-compose up --scale model_client_grpc=3 --scale model_client_rest=3
```
 
This will start the server with the pre-trained models, and start 3 of each clients that randomly request predictions from the model. Output look something like this:

````
Starting sklearn-model-server_model_server_grpc_1 ... done
Starting sklearn-model-server_minio_1        ... done
Starting sklearn-model-server_model_client_grpc_1 ... done
Creating sklearn-model-server_model_client_grpc_2 ... done
Creating sklearn-model-server_model_client_grpc_3 ... done
Creating sklearn-model-server_model_client_rest_1 ... done
Creating sklearn-model-server_model_client_rest_2 ... done
Creating sklearn-model-server_model_client_rest_3 ... done
[Minio stuff ...]
model_client_1  | ClientId: 40614
model_client_1  | X {
model_client_1  |   f0: -2.545633554458618
model_client_1  |   f1: -0.24103513360023499
model_client_1  |   f2: -1.0877643823623657
model_client_1  |   f3: -1.8311690092086792
model_client_1  |   f4: -0.1957949697971344
model_client_1  | }
model_client_1  | ModelName: "RandomForestClassifier.pkl"
[...]
model_client_2  | ClientId: 16356
model_client_2  | X {
model_client_2  |   f0: -2.180135488510132
model_client_2  |   f1: -3.1747219562530518
model_client_2  |   f2: -2.9947762489318848
model_client_2  |   f3: 0.9534611701965332
model_client_2  |   f4: -0.6837826371192932
model_client_2  | }
model_client_2  | ModelName: "SGDClassifier.pkl"
[...]
model_client_rest_1  | Client: 27472: Saved preds: data/data_test.hdf_client_27472_RandomForestClassifier.pkl_preds.csv
[...]
model_client_rest_2  | Client 16348: Returned path: data/data_test.hdf_client_16348_RandomForestClassifier.pkl_preds.csv in 1.29s
[... etc.]
````
 
 ### Individual containers
 
 #### Model-Server-GRPC
 (see also Model-Server-GRPC/README)  
 
Accepts gRPC requests for predictions, and returns the predicted probabilities. Full data is included in request and response.
 
Run:
  ```Bash
cd Model-Server-GRPC
sudo docker build . -t model_server_grpc
sudo docker run -p 8080:8080 model_server_grpc
 ```
 
 #### Model-Client-GRPC
 (see also Model-Client-GRPC/README)  
  
A simple service to emulate a client that randomly queries the server for predictions every few seconds.
 
Run:
 ```Bash
cd Model-Client-GRPC
sudo docker build . -t model_client_grpc
sudo docker run model_client_grpc
 ```
 
  #### Model-Server-REST
 (see also Model-Server-REST/README)  
 
Accepts REST requests for predictions, and returns the path to a file containing the predicted probabilities. Paths to files are included in request and response.
 
Run:
  ```Bash
cd Model-Server-REST
sudo docker build . -t model_server_rest
sudo docker run -p 8000:8000 -t -i model_server_rest
 ```
 
 #### Model-Client-REST
 (see also Model-Client-REST/README)  
  
A simple service to emulate a client that randomly queries the server for predictions every few seconds.
 
Run:
 ```Bash
cd Model-Client-REST
sudo docker build . -t model_client_rest
sudo docker run model_client_rest
 ```
 
 ### Model-Trainer
 Planned. Will replace the training scripts in Model-Server/model_server/scripts/, and save models (pickled and ONNYX) to Min.io for the Model-Server to use.
 
