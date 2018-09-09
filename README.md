# CMPE273-Lab2

## Lab 2 Assignment:
Create a simple calculator with add(x, y) function as a gRPC server and provide a test client to invoke the calculator service.

## Included files:
-adder.proto
-adder_client.py
-adder_server.py

## How to Run:

Generate adder_pb2 and adder_pb2_grpc files
```sh
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./adder.proto
```

Run Server
```sh
python adder_server.py

```

Run Client (In a Separate Tab)
```sh
python adder_client.py
This program will call add(x,y) as remote procedure
x=5
y=2
Adder client sending x=5 and y=2
Adder client received: 7.0
```
