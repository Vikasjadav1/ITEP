class Equal:
    def __init__(self,a):
        self.__a=a

    def __eq__(self,sd):
        ans=Equal(0)
        ans.temp=self.__a==sd.__a
        return ans

    def __str__(self):
        return str(self.temp)
    
d1=Equal(3)
d2=Equal(3)
d3=d1==d2 #d1.__add__(d2)
print(d3)