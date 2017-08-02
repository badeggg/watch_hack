from distutils.core import setup, Extension
import os

setup(
  name = 'watchmacdir',
  version = '1.0',
  description = "Watch directory change on mac.",
  ext_modules = [
    Extension('watchmacdir', sources = [os.path.dirname(os.path.abspath(__file__))+'/watchmacdir.c'], extra_link_args=["-framework","CoreFoundation",'-framework', 'CoreServices'])
  ]
)
