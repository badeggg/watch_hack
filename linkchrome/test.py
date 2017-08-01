import link as linkmodule
import json
import sys

Link = linkmodule.Link
ll = Link('chrome://newtab/')
inspect_json = ll.get_inspectable_pages()
json_obj = json.loads(inspect_json)
dumped_json = json.dumps(json_obj, indent=2, sort_keys=True)
print(dumped_json)

#sys.exit()

ws = ll.run()
ws.send('{"id":1,"method":"Network.enable","params":{"maxTotalBufferSize":10000000,"maxResourceBufferSize":5000000}}')
print(ws.recv())

