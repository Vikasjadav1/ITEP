class Movie:
    def __init__(self,name,seats):
        self.name=name
        self.seats=seats

    def available_seat(self):
        if self.seats>0:
            print(f"{self.seats} seats available. ")
        else:
            print("seats are full.")

    def book(self,ticket):
        if self.seats>=ticket:
            self.seats-=ticket
            print(f"{ticket} seats booked .......")
        else:
            print(f"booking cancelled * {self.seats} seats available........")

    def cancel(self,ticket):
        self.seats+=ticket
        print("seats cancelled.........")

    def seat_available(self):
        print(f"{self.seats} seats are available...")

m1=Movie("kgf",5)

m1.available_seat()
m1.book(5)
m1.cancel(5)
m1.book(2)
m1.seat_available()