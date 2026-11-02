class Greater:
    def __init__(self,a):
        self.__a=a

    def __gt__(self,sd):
        ans=Greater(0)
        ans.temp=self.__a>sd.__a
        return ans

    def __str__(self):
        return str(self.temp)
    
d1=Greater(1)
d2=Greater(2)
d3=d1>d2 #d1.__add__(d2)
print(d3)