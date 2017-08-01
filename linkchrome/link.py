from urllib import request
import json
import websocket

class Link:
  def __init__(self, target_page_url, port=9222):
    self.port = port
    self.target_page_url = target_page_url
    self.url_to_get_inspectable_pages = 'http://localhost:{}/json'.format(self.port)
  def get_inspectable_pages(self):
    ret = request.urlopen(self.url_to_get_inspectable_pages).read()
    return ret
  def get_target_page_websocket_url(self):
    pages = json.loads( self.get_inspectable_pages() )
    for page in pages:
      if page['url'] == self.target_page_url:
        ret = page['webSocketDebuggerUrl']
        break
    return ret
  def __ws_on_error(self, ws, error):
    print(error)
  def run(self):
    ws_url = self.get_target_page_websocket_url()
    ws = websocket.create_connection(ws_url, on_error = self.__ws_on_error)
    return ws
