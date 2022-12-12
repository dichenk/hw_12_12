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

x = MyInt(5)
print(x)
print(type(x + 6))
print(type(x * 10))
print(x*100/(-10))
