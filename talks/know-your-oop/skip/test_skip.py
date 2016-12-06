import skip


def test_mro_change():

    class A(object):

        def x(self):
            self.y()
            return 1

        def y(self):
            pass

    class B(A):

        def x(self):
            _ = skip.mro(self, B)
            return _.x()

        def y(self):
            raise Exception('We are here.')

    assert B().x() == 1


def test_skip_multiple_classes():

    class A(object):

        def x(self):
            return self.y() + self.z()

        def y(self):
            return 1

        def z(self):
            return 2

    class B(A):

        def x(self):
            raise Exception('We are here.')

        def y(self):
            raise Exception('We are here.')

        def z(self):
            raise Exception('We are here.')

    class C(B):

        def y(self):
            return 2

    class D(C):

        def x(self):
            _ = skip.mro(self, B, D)
            return _.x()

        def y(self):
            raise Exception('We are here.')

        def z(self):
            raise Exception('We are here.')

    assert D().x() == 4
