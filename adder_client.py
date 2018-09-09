from __future__ import print_function

import grpc

import adder_pb2
import adder_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = adder_pb2_grpc.AdderStub(channel)
        print("This program will call add(x,y) as remote procedure")
        x = input("x=")
        y = input("y=")
        print("Adder client sending x={} and y={}".format(x,y))
        response = stub.add(adder_pb2.AddRequest(x=x, y=y))
        print("Adder client received: " + str(response.result))


if __name__ == '__main__':
    run()
