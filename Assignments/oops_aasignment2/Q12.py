class Car:
    def __init__(self,car_num,price_per_day):
        self.car_num=car_num
        self.price_per_day=price_per_day
        self.available=True

    def rent_car(self):
        if self.available==True:
            self.available=False
            print("car rented successfully...........")
        else:
            print("car already rented .........")

    def return_car(self):
        if self.available==False:
            self.available=True
            print("car returned..........")
        else:
            print("car already returned....")

    def calculate_rent(self,day):
        print(f"{day} day rent price {self.price_per_day*day}")

car1=Car(1234,1000)
car1.rent_car()
car1.return_car()
car1.return_car()
car1.rent_car()
car1.calculate_rent(10)