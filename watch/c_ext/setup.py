from distutils.core import setup, Extension

setup(
  name = 'watchmacdir',
  version = '1.0',
  description = "Watch directory change on mac.",
  ext_modules = [
    Extension('watchmacdir', sources = ['watchmacdir.c'])
  ]
)
