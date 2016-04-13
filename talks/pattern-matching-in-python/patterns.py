# TODO:
# * tree example
# * fold should not relay on integers
# * ordered search for signatures (not for loop)
# * replace seq[0] with head and tail unboxing


import sys
from types import ModuleType


def match(*expressions, **keyword_expressions):

    def decorator(f):
        if f.__name__ not in f.__globals__:
            def wrapper(*args, **kwargs):
                for signature, f in wrapper.signatures:
                    if signature == (args, kwargs):
                        return f(*args, **kwargs)
                else:
                    raise Exception('Can not find appropriate pattern')
            wrapper.signatures = []
        else:
            wrapper = f.__globals__[f.__name__]

        signature = Signature(*expressions, **keyword_expressions)
        wrapper.signatures.append((signature, f))
        return wrapper

    return decorator


class Signature:

    def __init__(self, *args, **kwargs):

        self.args = args
        self.kwargs = kwargs

    def __eq__(self, other):

        args, kwargs = other
        return args == self.args and kwargs == self.kwargs


class Expression:

    def __gt__(self, other):

        return GreaterPredicate(other)

    def __getitem__(self, item):

        return HeadPredicate(item)

    def __eq__(self, other):

        return True


class Predicate:

    def __init__(self, *args, **kwargs):

        self.args = args
        self.kwargs = kwargs


class GreaterPredicate(Predicate):

    def __eq__(self, other):

        return isinstance(other, type(self.args[0])) and other > self.args[0]


class HeadPredicate(Predicate):

    def __eq__(self, other):

        return isinstance(other, list) and len(other) >= self.args[0] + 1


class module(ModuleType):

    def __getattr__(self, name):

        if name == 'match':
            return match
        else:
            return Expression()


old_module = sys.modules['patterns']

new_module = sys.modules['patterns'] = module('patterns')
