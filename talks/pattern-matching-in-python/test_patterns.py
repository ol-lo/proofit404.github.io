from patterns import match, _, x, l


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


@match(x > 5)
def greater_test(x):
    return '{} greater then five'.format(x)


@match(_)
def greater_test(x):
    return '{} less then or equal to five'.format(x)


assert greater_test(7) == '7 greater then five'
assert greater_test(1) == '1 less then or equal to five'


# List test.


@match(_, [])
def fold(f, seq):
    return 0


@match(_, l[0])
def fold(f, seq):
    return f(seq[0], fold(f, seq[1:]))


assert fold(lambda x, y: x + y, [1, 2, 3, 4, 5]) == 15
