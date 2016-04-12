class Declaration:

    def __getitem__(self, item):
        if isinstance(item, slice):
            return item
        else:
            return slice(item, None, None)


class Expression:

    def __init__(self, *args, **kwargs):

        self.args = args
        self.kwargs = kwargs

    def match(self, *args, **kwargs):

        return self.match_args(args) and kwargs == self.kwargs

    def match_args(self, args):

        if len(self.args) != len(args):
            return False
        for num, arg in enumerate(self.args):
            if arg is any:
                continue
            elif isinstance(arg, slice):
                try:
                    args[num][arg.start]
                except KeyError:
                    return False
            elif arg != args[num]:
                return False
        else:
            return True


def match(*exp, **kwexp):

    def decorator(f):

        if f.__name__ not in globals():
            def wrapper(*args, **kwargs):
                for expression, f in wrapper.patterns:
                    if expression.match(*args, **kwargs):
                        return f(*args, **kwargs)
                else:
                    raise Exception('Can not find appropriate pattern')
            wrapper.patterns = []
        else:
            wrapper = globals()[f.__name__]

        wrapper.patterns.append((Expression(*exp, **kwexp), f))
        return wrapper

    return decorator


# Simple test.


@match(1)
def test(x):
    return 'one'


@match(2)
def test(x):
    return 'two'


assert test(1) == 'one'
assert test(2) == 'two'


# List test.


lst = Declaration()


@match(any, [])
def fold(f, lst):
    return 0


@match(any, lst[0])
def fold(f, lst):
    return f(lst[0], fold(f, lst[1:]))


def add(x, y):
    return x + y


assert fold(add, [1, 2, 3, 4, 5]) == 15
