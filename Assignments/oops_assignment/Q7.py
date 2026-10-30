'''
Create a class Student with fields: name, mathMarks, scienceMarks.
Use setters to assign values. Add a method getAverage().
'''

class Student:
    def set_name(self,name):
        self.__name=name
    def set_mathMarks(self,mathMarks):
        self.__mathMarks=mathMarks
    def set_scienceMarks(self,scienceMarks):
        self.__scienceMarks=scienceMarks
    
    def average(self):
        average=(self.__mathMarks+self.__scienceMarks)/2
        return average
    
    def display(self):
        print(f"name : {self.__name}")

obj=Student()
obj.set_name("vikas")
obj.set_mathMarks(65)
obj.set_scienceMarks(48)
average=obj.average()
print(f"average {average}")
obj.display()

     