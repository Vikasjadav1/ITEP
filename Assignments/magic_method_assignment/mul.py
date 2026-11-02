class Mul:
    def __init__(self,a):
        self.__a=a

    def __mul__(self,sd):
        temp=Mul(0)
        temp.__a=self.__a*sd.__a
        return temp

    def __str__(self):
        return str(self.__a)
    
d1=Mul(5)
d2=Mul(2)
d3=d1*d2 #d1.__add__(d2)
print(d3)