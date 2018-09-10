# CMPE273-Lab2

## Lab 2 Assignment:
Create a simple calculator with add(x, y) function as a gRPC server and provide a test client to invoke the calculator service.

## Included files:
- calculator.proto
- calculator_client.py
- calculator_server.py

- calculator_pb2.py
- calculator_pb2_grpc.py

## How to Run:

Generate calculator_pb2 and calculator_pb2_grpc files
```sh
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./calculator.proto
```

Run Server
```sh
python calculator_server.py

```

Run Client (In a Separate Tab)
```sh
python calculator_client.py
This program will call add(x,y) as remote procedure
x=5
y=2
Calculator client sending x=5 and y=2
Calculator client received: 7.0
```
