import skip


class A:

    def x(self):
        self.y()

    def y(self):
        pass


class B(A):

    def x(self):
        print('Enter X')
        super(B, self).x()
        print('Exit X')

    def y(self):
        print('Enter Y')
        super(B, self).y()
        print('Exit Y')


class C(A):

    def x(self):
        print('Enter X')
        skip.mro(self, C).x()
        print('Exit X')

    def y(self):
        print('Enter Y')
        skip.mro(self, C).y()
        print('Exit Y')
