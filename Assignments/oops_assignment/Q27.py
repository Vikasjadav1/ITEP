'''
 Write a Java program to create a class called "Movie" with attributes for title, director, actors, 
 and reviews, and methods for adding and retrieving reviews.
 '''

class Movie:
    def __init__(self,title,director,actors):
        self.__title=title
        self.__director=director
        self.__actors=actors
        self.__review=[]

    def add_review(self,review):
        self.__review.append(review)

    def get_review(self):
        print("................reviews.................")
        if len(self.__review)==0:
            print("no reviews...............")
        for review in self.__review:
            print(review)


obj=Movie("pk","Rajkumar Hirani",["Aamir Khan", "R. Madhavan", "Sharman Joshi"])
obj.add_review("amazing movie")
obj.add_review("good movie")
obj.add_review("amazing movie")
obj.get_review()
