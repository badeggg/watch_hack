#include <Python.h>
#include <CoreServices/CoreServices.h>

static PyObject*
watchmacdir_watch(PyObject* self, PyObject* args)
{
  printf("watching...\n");
  return PyLong_FromLong(0);
}

static PyMethodDef watchMethods[] = 
{
  {"watch", watchmacdir_watch, METH_VARARGS, "Watch directory change."},
  {NULL, NULL, 0, NULL}
};

static struct PyModuleDef watchmacdirmodule =
{
  PyModuleDef_HEAD_INIT,
  "watchmacdir",
  NULL,
  -1,
  watchMethods
};

PyMODINIT_FUNC
PyInit_watchmacdir(void)
{
  return PyModule_Create(&watchmacdirmodule);
}
