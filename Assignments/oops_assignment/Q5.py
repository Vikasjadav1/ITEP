'''
Create a class Movie with fields: name, genre, and rating.
Use setters and create a method isHit() that returns true if rating ≥ 8.0.
'''
class Movie:
    def set_name(self,name):
        self.__name=name

    def set_rating(self,rating):
        self.__rating=rating

    def isHit(self):
        if self.__rating>=8.0:
            return True
    
obj=Movie()
obj.set_name("pk")
obj.set_rating(9)

hit=obj.isHit()
print(hit)