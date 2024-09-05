# PyBurp

## install 
pip install PyBurp

## Basic
```python
import PyBurp 

def test(a,b,c,d,e):
    print(a,type(a),b,type(b),c,type(c),d,type(d),e,type(e))
    return b'asdf'


@PyBurp.expose # some thing wrong. not always work
def test2():
    return 'xxx'

PyBurp.expose(test) # recommend
PyBurp.run("127.0.0.1:30051")
```


## Frida

```python
import PyBurp 
import time
import frida

def my_message_handler(message, payload):
    print(message)
    print(payload)

def decrypt(arg):
    print(f"decrypt {arg}")
    return script.exports.calldecryptfunction(arg)


def encrypt(arg):
    print(f"encrypt {arg}")
    return script.exports.callencryptfunction(arg)

# device = frida.get_usb_device()
device = frida.get_device_manager().add_remote_device('127.0.0.1:27042')

# pid = device.spawn(["com.example.www"])
# device.resume(pid)
# time.sleep(1)  # Without it Java.perform silently fails
# session = device.attach(pid)

session = device.attach(17982)
with open("python_to_call_function.js") as f:
    script = session.create_script(f.read())
script.on("message", my_message_handler)
script.load()

print(encrypt("test"))
print(decrypt(encrypt("test")))

PyBurp.expose(decrypt)
PyBurp.expose(encrypt)

PyBurp.run("127.0.0.1:30051")

```



