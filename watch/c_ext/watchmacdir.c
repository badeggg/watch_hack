#include <Python.h>
#include <CoreServices/CoreServices.h>

PyObject* callback = NULL;

void mycallback(
    ConstFSEventStreamRef streamRef,
    void *clientCallBackInfo,
    size_t numEvents,
    void *eventPaths,
    const FSEventStreamEventFlags eventFlags[],
    const FSEventStreamEventId eventIds[])
{
    PyObject_CallObject(callback, NULL);
}

static PyObject*
watchmacdir_watch(PyObject* self, PyObject* args)
{
  const char* path;
  float latency = 0.05;
  FSEventStreamRef stream;
  if(!PyArg_ParseTuple(args, "sO|f", &path, &callback, &latency))
  {
    return NULL;
  }

  //Create event stream
  CFStringRef pathStrRef = CFStringCreateWithCString(NULL, path, kCFStringEncodingUTF8);
  CFArrayRef pathsToWatch = CFArrayCreate(NULL, (const void **)&pathStrRef, 1, NULL);
  stream = FSEventStreamCreate(
    NULL,
    //(FSEventStreamCallback)&callback,
    &mycallback,
    NULL,
    pathsToWatch,
    kFSEventStreamEventIdSinceNow,
    latency,
    kFSEventStreamCreateFlagNone
  );

  //Schedule stream to run loop
  FSEventStreamScheduleWithRunLoop(stream, CFRunLoopGetCurrent(), kCFRunLoopDefaultMode);
  FSEventStreamStart(stream);
  printf("Watching %s with latency %f...\n", path, latency);
  CFRunLoopRun();

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
