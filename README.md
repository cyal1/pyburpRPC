# pyburpRPC

## python

### install
pip install pyburp

### example
```python
import pyburp 

def test(a,b,c,d,e):
    print(a,type(a),b,type(b),c,type(c),d,type(d),e,type(e))
    return b'asdf'


@pyburp.expose
def test2():
    return 'xxx'

pyburp.expose(test)
pyburp.run("127.0.0.1:30051")
```
