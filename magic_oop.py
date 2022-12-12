from sympy import *
import math

class Derivative:
    def __init__(self, func):
        self.__func = func

    def __call__(self, *args, **kwargs):
        return diff(self.__func(x)).subs(x, args[0])

# Просто считаем синус
def sin_(x):
    return sin(x)

print(sin_(math.pi/3))
#0.8660254037844386

# Считаем производную
@Derivative
def sin__(x):
    return sin(x)

x = Symbol('x')

print(sin__(math.pi/3))
#0.4999566978958203
