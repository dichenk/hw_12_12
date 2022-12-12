from sympy import * ## функцию diff для расчета производной возьмем из этой библиотеки
import math

x = Symbol('x') ## нужно для производной

class Derivative:
    def __init__(self, func):
        self.__func = func

    def __call__(self, *args, **kwargs):
        return diff(self.__func(x)).subs(x, args[0])

def sin1_(x):
    return sin(x)

@Derivative
def sin2_(x):
    return sin(x)

print(sin1_(math.pi/3)) #0.8660254037844386
print(sin2_(math.pi/3)) #0.4999566978958203
