'''
 Write a Java program to create class called "TrafficLight" with attributes for color and duration, and methods to change the color and check for red or green.'''
  
class TrafficLight:
    def __init__(self,color,duration):
        self.__color=color
        self.__duration=duration


    def check_red(self):
        if self.__color=="red":
            print("RED color..............")

    def check_green(self):
        if self.__color=="green":
            print("Green color..............")

    def change_color(self,color):
        self.__color=color
        print(f"color changed {self.__color}")

obj=TrafficLight("red",10)
obj.check_red()
obj.check_green()
obj.change_color("green")