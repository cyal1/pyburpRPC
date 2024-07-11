from pychrome import Browser
from pychrome.cli import JSONTabEncoder
import json
import BcryptRpcServer

def getTabById(tabs, tab_id):
    for tab in tabs:
        if tab.id == tab_id:
            return tab
    return None

browser = Browser(url="http://localhost:9222")

try:
    tabs = browser.list_tab()
except Exception as e:
    print(e, "\n\nYou need run chrome with debugging mode:\n/Applications/Google\\ Chrome.app/Contents/MacOS/Google\\ Chrome --remote-debugging-port=9222\n")
    exit(-1)

index = 1
tab_map = {}
for tab in json.loads(json.dumps(tabs, cls=JSONTabEncoder, indent=4)):
    print(index, tab.get("id"), tab.get("title"), tab.get("url"))
    tab_map[index] = tab.get("id")
    index += 1

input_num = int(input("Choice the tab number: "))
target_id = tab_map[input_num]

tab = getTabById(tabs, target_id)

if tab is None:
    print("Not found tab: ", target_id)
    exit(-1)

tab.start()

def decrypt(i, s):
    js_expr = f"test({i},{json.dumps(s)})"
    print("call: ", js_expr)
    result = tab.call_method("Runtime.evaluate", expression = js_expr).get("result")
    # print(result)
    if result.get("subtype") == "error":
        disc = result.get("description")
        print(disc)
        return disc
    r = json.dumps(result.get("value"))
    print(f"result{type(r)}: ", r)
    return r

decrypt(101, "askdlljglaksjdgasdg'\"adlskjgasjdg;\n;alksjg")

BcryptRpcServer.expose(decrypt)
BcryptRpcServer.run("127.0.0.1:30051")

