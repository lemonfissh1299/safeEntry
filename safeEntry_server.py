from concurrent import futures
import time

import grpc 
import safeEntry_pb2
import safeEntry_pb2_grpc

class safeEntryServicer(safeEntry_pb2_grpc.safeEntryServicer):
    def CheckIn(self, request, context):
        print("Check-In Request Made: ")
        # return super().CheckIn(request, context)
    
    def CheckOut(self, request, context):
        print("Check-Out Request Made: ")
        # return super().CheckOut(request, context)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers= 30))
    safeEntry_pb2_grpc.add_safeEntryServicer_to_server(safeEntryServicer(), server)
    server.add_insecure_port("localhost:50051")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()