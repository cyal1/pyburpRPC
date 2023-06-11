# BcryptRpcServer
```python
import BcryptRpcServer 

def test(a,b,c,d,e):
    print(a,type(a),b,type(b),c,type(c),d,type(d),e,type(e))
    return b'asdf'


@BcryptRpcServer.expose
def test2():
    return 'xxx'
    
BcryptRpcServer.expose(test)
BcryptRpcServer.run("127.0.0.1:30051")
```
