import sys


def set_trace():
    sys.settrace(dispatch)


def dispatch(frame, event, arg):
    print(event, list([x for x in dir(frame) if not x.startswith('__')]))
    return dispatch
