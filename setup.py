from setuptools import setup, find_packages
import time
import os
import subprocess
from textwrap import dedent

#install c-extension watchmacdir
if not subprocess.run(['which', 'python3']).returncode == 0:
  print(("""
  \033[91m
  {}
  Please install watchmacdir module manually by run: "[your python3.X command] watch/c_ext/setup.py install" in watch_hack project root directory
  Tip: watchmacdir module is a c-extension module to monitor directory change. "watchmacdir" is writted in this project
  {}
  \033[0m
  """).format('+'*100,'+'*100))
else:
  os.system('python3 watch/c_ext/setup.py install')

#install watch_hack
setup(
    name="watch_hack",
    version="0.1",
    install_requires=[
        'websocket-client',
    ],
)

#set alias
if not subprocess.run(['which', 'python3']).returncode == 0:
  print(("""
  \033[91m
  {}
  Please set alias manually by add this two line to your ~/.bash_profile (replace content in [] with proper text):
      alias watch_hack='python3 [directory where you put this project in]/start.py'
      alias wah='watch_hack'
  {}
  \033[0m
  """).format('+'*100,'+'*100))
else:
  bash_file_position =  os.path.expanduser('~')+'/.bash_profile'
  os.system('touch '+bash_file_position)
  bash_profile = open(bash_file_position, 'a')
  bash_profile.write(
      dedent("""
      alias watch_hack='python3 {}/start.py'
      alias wah='watch_hack'
      """).format( os.path.dirname(os.path.abspath(__file__)) )
    )