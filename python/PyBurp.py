import grpc
import google.protobuf.any_pb2 as any_pb2
from google.protobuf.wrappers_pb2 import *
import burpextender_pb2 as pb2
from concurrent import futures
import burpextender_pb2_grpc as pb2_grpc
import socket


def is_port_in_use(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        result = sock.connect_ex((host, port))
        return result == 0

function_registry = {}

def expose(func):
    function_registry[func.__name__] = func

class CallFuncServicer(pb2_grpc.CallFuncServiceServicer):
    def CallFunc(self, request, context):
        try:
            func_name = request.func_name
            args = [self.convert_arg(arg) for arg in request.args]
            print(f"function '{func_name}()' with arguments list {args}")
            result = None
            try:
               func = function_registry[func_name]
            except KeyError:
               raise ValueError(f"No function named '{func_name}' defined.")
            result = func(*args)

            if result is None:
                response = pb2.Response(res=any_pb2.Any())
            elif isinstance(result, str):
                value = StringValue(value=result)
                any_obj = any_pb2.Any()
                any_obj.Pack(value)
                response = pb2.Response(res=any_obj)
            elif isinstance(result, bool):
                value = BoolValue(value=result)
                any_obj = any_pb2.Any()
                any_obj.Pack(value)
                response = pb2.Response(res=any_obj)
            elif isinstance(result, int):
                value = Int64Value(value=result)
                any_obj = any_pb2.Any()
                any_obj.Pack(value)
                response = pb2.Response(res=any_obj)
            elif isinstance(result, float):
                value = DoubleValue(value=result)
                any_obj = any_pb2.Any()
                any_obj.Pack(value)
                response = pb2.Response(res=any_obj)
            elif isinstance(result, bytes):
                value = BytesValue(value=result)
                any_obj = any_pb2.Any()
                any_obj.Pack(value)
                response = pb2.Response(res=any_obj)
            else:
                raise ValueError(f"Invalid result type: {type(result)}, only allowed str,bool,int,float,bytes")

            return response
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(str(e))
            return pb2.Response()

    def convert_arg(self, arg):
        value = None
        if arg.Is(BoolValue.DESCRIPTOR):
            bool_value = BoolValue()
            arg.Unpack(bool_value)
            value = bool_value.value
        elif arg.Is(Int64Value.DESCRIPTOR):
            int32_value = Int64Value()
            arg.Unpack(int32_value)
            value = int32_value.value
        elif arg.Is(StringValue.DESCRIPTOR):
            string_value = StringValue()
            arg.Unpack(string_value)
            value = string_value.value
        elif arg.Is(DoubleValue.DESCRIPTOR):
            double_value = DoubleValue()
            arg.Unpack(double_value)
            value = double_value.value
        elif arg.Is(BytesValue.DESCRIPTOR):
            bytes_value = BytesValue()
            arg.Unpack(bytes_value)
            value = bytes_value.value
        else:
            value = arg
        return value

def run(bind="127.0.0.1:50051"):
    
    host, port = bind.split(":")
    port = int(port)
    
    if is_port_in_use(host, port):
        print(f"Port {port} is already in use.")
        return

    server = grpc.server(futures.ThreadPoolExecutor())
    pb2_grpc.add_CallFuncServiceServicer_to_server(CallFuncServicer(), server)
    server.add_insecure_port(bind)  # Replace with the appropriate port
    print(f"PyBurp listening on {bind}")
    server.start()
    server.wait_for_termination()

