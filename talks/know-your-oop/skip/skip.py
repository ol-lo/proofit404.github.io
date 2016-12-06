def mro(instance, *classes):

    class SkipType(type):

        def mro(cls):
            old = instance.__class__.__mro__
            new = tuple([x for x in old if x not in classes])
            return new

    Skip = SkipType('Skip', (), {})
    return Skip()
