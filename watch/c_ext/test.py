import watchmacdir
import os
import time
from threading import Thread

def handler():
  print(" ❤️ 旭旭")
# def thread_watch():
#   watchmacdir.watch(os.getcwd(), handler, 0.1)
# t = Thread(target=thread_watch)
# t.start()

watchmacdir.watch(os.getcwd(), handler, 0.1)

