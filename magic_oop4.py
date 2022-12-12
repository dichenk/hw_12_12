class MyInt:
    def __init__(self, val):
        self.__val = self.__check(val)

    def __str__(self):
        return str(self.__val)

    def __repr__(self): 
        return f'{self.__class__}, {self.name}'
    
    @staticmethod
    def __check(val):
        return int(val)

    @staticmethod
    def __st(val):
        return str(val)

    def __add__(self, other):
        return MyInt(self.__val + self.__check(other))

    def __radd__(self, other):
        return MyInt(self.__val + self.__check(other))

    def __sub__(self, other):
        return MyInt(self.__val - self.__check(other))

    def __mul__(self, other):
        return MyInt(self.__val * self.__check(other))

    def __truediv__(self, other):
        return MyInt(self.__val / self.__check(other))

    def __eq__(self, other):
        return bytes(self.__st(self), encoding = 'utf-8') == bytes(other, encoding = 'utf-8')
    
    def __ne__(self, other):
        return bytes(self.__st(self), encoding = 'utf-8') != bytes(self.__st(other), encoding = 'utf-8')

    def __lt__(self, other):
        return bytes(self.__st(self), encoding = 'utf-8') < bytes(self.__st(other), encoding = 'utf-8')

    def __le__(self, other):
        return bytes(self.__st(self), encoding = 'utf-8') <= bytes(self.__st(other), encoding = 'utf-8')

    def __gt__(self, other):
        return bytes(self.__st(self), encoding = 'utf-8') > bytes(self.__st(other), encoding = 'utf-8')

    def __ge__(self, other):
        return bytes(self.__st(self), encoding = 'utf-8') >= bytes(self.__st(other), encoding = 'utf-8')



x = MyInt(5)
print(x < 3)
print(x == '5')
print(x >= '3')
print(x < '3')
