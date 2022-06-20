import grpc
import safeEntry_pb2
import safeEntry_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = safeEntry_pb2_grpc.safeEntryStub(channel)
        print ("1 => Check-In")
        print ("2 => Check-Out")
        print ("3 => History")
        print ("4 => Save/Restore SafeEntry state")
        rpc_call = input("What action: ")

        if rpc_call == "1":
            print ("Not implemented")

        if rpc_call == "2":
            print ("Not implemented")
        
        if rpc_call == "3":
            print ("Not implemented")
        
        if rpc_call == "4":
            print ("Not implemented")


if __name__ == "__main__":
    run()