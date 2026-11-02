class Lesser:
    def __init__(self,a):
        self.__a=a

    def __lt__(self,sd):
        ans=Lesser(0)
        ans.temp=self.__a<sd.__a
        return ans

    def __str__(self):
        return str(self.temp)
    
d1=Lesser(3)
d2=Lesser(2)
d3=d1<d2 #d1.__add__(d2)
print(d3)