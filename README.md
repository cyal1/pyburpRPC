# PyBurp

## python

### install
pip install PyBurp

### example
```python
import PyBurp 

def test(a,b,c,d,e):
    print(a,type(a),b,type(b),c,type(c),d,type(d),e,type(e))
    return b'asdf'


@PyBurp.expose
def test2():
    return 'xxx'

PyBurp.expose(test)
PyBurp.run("127.0.0.1:30051")
```
