from __future__ import print_function

import grpc

import calculator_pb2
import calculator_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = calculator_pb2_grpc.CalculatorStub(channel)
        print("This program will call add(x,y) as remote procedure")
        x = input("x=")
        y = input("y=")
        print("Calculator client sending x={} and y={}".format(x,y))
        response = stub.add(calculator_pb2.AddRequest(x=x, y=y))
        print("Calculator client received: " + str(response.result))


if __name__ == '__main__':
    run()
