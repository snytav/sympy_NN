from sympy import *


class f(Function):
    @classmethod
    def eval(cls, x, y=1, *args):
        return None




if __name__ == '__main__':
    x = symbols('x')
    df = diff(f,x)

    print(f(1).args)

    print(f(1, 2).args)

    print(f(1, 2, 3).args)