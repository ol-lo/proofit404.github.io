def match(*expressions, **keyword_expressions):

    def decorator(f):

        if f.__name__ not in globals():
            def wrapper(*args, **kwargs):
                for signature, f in wrapper.signatures:
                    if signature == (args, kwargs):
                        return f(*args, **kwargs)
                else:
                    raise Exception('Can not find appropriate pattern')
            wrapper.signatures = []
        else:
            wrapper = globals()[f.__name__]

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


# Simple test.


@match(1)
def test(x):
    return 'one'


@match(2)
def test(x):
    return 'two'


assert test(1) == 'one'
assert test(2) == 'two'


# Greater test.


_ = Expression()
x = Expression()


@match(x > 5)
def greater_test(x):
    return '{} greater then five'.format(x)


@match(_)
def greater_test(x):
    return '{} less then or equal to five'.format(x)


assert greater_test(7) == '7 greater then five'
assert greater_test(1) == '1 less then or equal to five'


# List test.


lst = Expression()


@match(_, [])
def fold(f, lst):
    return 0


@match(_, lst[0])
def fold(f, lst):
    return f(lst[0], fold(f, lst[1:]))


def add(x, y):
    return x + y


assert fold(add, [1, 2, 3, 4, 5]) == 15
