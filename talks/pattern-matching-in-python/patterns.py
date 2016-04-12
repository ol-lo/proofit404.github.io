class Expression:

    def __init__(self, *args, **kwargs):

        self.args = args
        self.kwargs = kwargs

    def match(self, *args, **kwargs):

        return args == self.args and kwargs == self.kwargs


def match(expression):

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

        wrapper.patterns.append((Expression(expression), f))
        return wrapper

    return decorator


@match(1)
def test(x):
    return 'one'


@match(2)
def test(x):
    return 'two'


assert test(1) == 'one'
assert test(2) == 'two'
