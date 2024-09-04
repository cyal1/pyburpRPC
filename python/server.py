import BcryptRpcServer

def test():
	return None

BcryptRpcServer.expose(test)
BcryptRpcServer.run("127.0.0.1:30051")
