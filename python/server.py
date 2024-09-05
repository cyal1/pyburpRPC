import PyBurp

def test():
	return None

PyBurp.expose(test)
PyBurp.run("127.0.0.1:30051")
