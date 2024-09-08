import pyburp

def test(s):
	print(s, type(s))
	return None

pyburp.expose(test)
pyburp.run("127.0.0.1:30051")
