import sys
import linecache


def set_trace():
    sys.settrace(dispatch)


def dispatch(frame, event, arg):
    line = linecache.getline(
        frame.f_code.co_filename,
        frame.f_lineno,
    )
    print(line.strip())
    return dispatch
