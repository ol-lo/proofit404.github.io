def foo(a, b):
    c = a + b
    d = c + a
    e = d + a


def bar():
    pass


import mydb
mydb.set_trace()
foo(1, 2)
pass
pass
bar()
