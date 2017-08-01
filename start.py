import watchmacdir
import sys
import re
import os
from launchrome import launch
from linkchrome.link import Link
from threading import Thread, Event
import time
from urllib import request

argv_str = ' '.join(sys.argv)

m=re.search('port=(\d+)', argv_str)
port = 9222 if not m else m.groups()[0]

m=re.search('page=([\w\.]+)', argv_str)
page = 'test.html' if not m else m.groups()[0]

page_url = 'file://{}/{}'.format(os.getcwd(), page)
cmd_reload = """
  {
    "id": 61,
    "method": "Runtime.evaluate",
    "params": {
      "expression": "location.reload();",
      "objectGroup": "console",
      "includeCommandLineAPI": true,
      "silent": false,
      "returnByValue": false,
      "generatePreview": true,
      "userGesture": true,
      "awaitPromise": false
    }
  }
"""

chrome = Thread(target=launch.run, args=(port, page))
chrome.start()
#poll request to check chrome has started
poll_url = 'http://localhost:{}/json'.format(port)
while True:
  try:
    request.urlopen(poll_url)
  except:
    print('Starting chrome...')
    time.sleep(0.3)
    continue
  break



print('-'*150)
ws = Link(page_url, port).run()
print('-'*150)


def reload_page():
  print('reloading page.....')
  ws.send(cmd_reload)
  print(ws.recv())
  print('page reloaded.')
  
watchmacdir.watch(os.getcwd(), reload_page, 0.1)
