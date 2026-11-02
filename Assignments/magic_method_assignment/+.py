class Plus:
    def __init__(self,a):
        self.__a=a

    def __add__(self,sd):
        temp=Plus(0)
        temp.__a=self.__a+sd.__a
        return temp

    def __str__(self):
        return str(self.__a)
    
d1=Plus(1)
d2=Plus(2)
d3=d1+d2 #d1.__add__(d2)
print(d3)
