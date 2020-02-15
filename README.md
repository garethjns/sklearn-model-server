# sklearn-model-server

A small set of Dockerized microservices for training and serving sklearn models over gRPC. Currently includes a server and a client that hassles the server for predictions. The server includes pre-trained models on generated data. In future the training will be moved to a separate service which will receive data save the data and trained models to minio.  
 
 
 ## Running
Running the whole system requires docker and docker-compose, running the individual services just requires docker.

Running all services (1 server + 3 clients + Minio).
 ```bash
docker-compose build
docker-compose up --scale model_client=3
```
 
This will start the server with the pre-trained models, and start 3 clients that randomly request predictions from the model. Output look something like this:

````
Starting sklearn-model-server_model_server_1 ... done
Starting sklearn-model-server_minio_1        ... done
Starting sklearn-model-server_model_client_1 ... done
Creating sklearn-model-server_model_client_2 ... done
Creating sklearn-model-server_model_client_3 ... done
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
[... etc.]
````
 
 
 ## Model-Server
 (see also Model-Server/README)  
 
Accepts gRPC requests for predictions, and returns the predicted probability.
 
Run:
  ```Bash
cd Model-Server
docker build . -t model_server
docker run -p 8080:8080 model_server
 ```
 
 ## Model-Client
 (see also Model-Client/README)  
  
A simple service to emulate a client that randomly queries the server for predictions every few seconds.
 
Run:
 ```Bash
cd Model-Client
docker build . -t model_client
docker run model_client
 ```
 
 ## Model-Trainer
 Planned. Will replace the training scripts in Model-Server/model_server/scripts/, and save models (pickled and ONNYX) to Minio for the Model-Server to use.
 