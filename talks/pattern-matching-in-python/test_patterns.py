from patterns import match, Expression


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
