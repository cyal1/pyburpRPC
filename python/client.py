import grpc
import google.protobuf.any_pb2 as any_pb2
import burpextender_pb2 as pb2
from google.protobuf.wrappers_pb2 import *
import burpextender_pb2_grpc as pb2_grpc


def call_func_service():
    channel = grpc.insecure_channel('localhost:30051')  # Replace with the appropriate address and port
    stub = pb2_grpc.CallFuncServiceStub(channel)

    # Create the request message with the function name and arguments
    func_name = "test"

    value = Int64Value(value=1)
    any_obj = any_pb2.Any()
    any_obj.Pack(value)

    args = [
        any_obj,
        any_obj,
        any_obj,
        any_obj,
        any_obj,
    ]
    request = pb2.Request(func_name=func_name, args=args)

    # Invoke the remote function
    res = stub.CallFunc(request).res

    if res.Is(Int64Value.DESCRIPTOR):
        int32_value = Int64Value()
        res.Unpack(int32_value)
        value = int32_value.value
    elif res.Is(BoolValue.DESCRIPTOR):
        bool_value = BoolValue()
        res.Unpack(bool_value)
        value = bool_value.value
    elif res.Is(StringValue.DESCRIPTOR):
        string_value = StringValue()
        res.Unpack(string_value)
        value = string_value.value
    elif res.Is(DoubleValue.DESCRIPTOR):
        double_value = DoubleValue()
        res.Unpack(double_value)
        value = double_value.value
    elif res.Is(BytesValue.DESCRIPTOR):
        bytes_value = BytesValue()
        res.Unpack(bytes_value)
        value = bytes_value.value
    else:
        value = res
        
    print(value, type(value))


if __name__ == '__main__':
    call_func_service()
