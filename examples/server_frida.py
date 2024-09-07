import pyburp
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

# pid = device.spawn(["com.wifi.reader.jinshu"])
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


pyburp.expose(decrypt)
pyburp.expose(encrypt)

pyburp.run("127.0.0.1:30051")

# command = ""
# while 1 == 1:
#     command = input("Enter command:\n1: Exit\n2: Call Encrypt function\n3: Call Decrypt function\nchoice:")
#     if command == "1":
#         break
#     elif command == "2":
#         arg = input("Enter arg: ")
#         encrypt_text = script.exports.callencryptfunction(arg)
#         print(type(encrypt_text))
#         print("Encrypted String: ",encrypt_text)
#     elif command == "3":
#         arg = input("Enter arg: ")
#         plain_text = script.exports.calldecryptfunction(arg)
#         print("Decrypted String: ",plain_text)

