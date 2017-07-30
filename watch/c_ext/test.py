import watchmacdir
import os
import time

def handler():
  print(" ❤️ ")
watchmacdir.watch(os.getcwd(), handler, 0.1)
os.system('touch ii')
time.sleep(3)
