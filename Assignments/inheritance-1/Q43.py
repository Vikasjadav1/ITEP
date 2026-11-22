
class Passenger:
    def __init__(self, id, name, age, gender):
        self.__id = id
        self.__name = name
        self.__age = age
        self.__gender = gender

    def display(self):
        print("ID:", self.__id)
        print("Name:", self.__name)
        print("Age:", self.__age)
        print("Gender:", self.__gender)


class Train:
    trains = []

    def __init__(self, train_number, train_name, source, destination, available_seats, ticket_price):
        self.__train_number = train_number
        self.__train_name = train_name
        self.__source = source
        self.__destination = destination
        self.__available_seats = available_seats
        self.__ticket_price = ticket_price

        Train.trains.append(self)

    @classmethod
    def display_trains(cls):
        for train in cls.trains:
            print("\nTrain Number:", train.__train_number)
            print("Train Name:", train.__train_name)
            print("Source:", train.__source)
            print("Destination:", train.__destination)
            print("Available Seats:", train.__available_seats)
            print("Ticket Price:", train.__ticket_price)

    def check_seats(self, seats):
        if self.__available_seats >= seats and seats > 0:
            return True
        else:
            return False


class Ticket:
    def __init__(self, pnr, passenger, train, seats):
        self.__pnr = pnr
        self.__passenger = passenger
        self.__train = train
        self.__seats = seats
        self.__total_fare = 0

    def calculate_fare(self):
        self.__total_fare = self.__train._Train__ticket_price * self.__seats
        return self.__total_fare

    def book_ticket(self):
        if self.__train.check_seats(self.__seats):
            self.__train._Train__available_seats -= self.__seats
            self.calculate_fare()
            print("Ticket booked successfully!")
            return True
        else:
            print("Seats not available!")
            return False

    def display_ticket(self):
        print("\n----- TICKET DETAILS -----")
        print("PNR:", self.__pnr)

        self.__passenger.display()

        print("Train Name:", self.__train._Train__train_name)
        print("Number of Seats:", self.__seats)
        print("Total Fare:", self.__total_fare)


t1 = Train(12951, "Rajdhani Express", "Indore", "Delhi", 50, 800)
t2 = Train(12952, "Mumbai Express", "Indore", "Mumbai", 30, 600)
t3 = Train(12953, "Shatabdi Express", "Bhopal", "Delhi", 40, 500)

Train.display_trains()

id = int(input("\nEnter Passenger ID: "))
name = input("Enter Name: ")
age = int(input("Enter Age: "))
gender = input("Enter Gender: ")

p1 = Passenger(id, name, age, gender)

train_no = int(input("Enter Train Number: "))
seats = int(input("Enter Seats: "))

for train in Train.trains:
    if train._Train__train_number == train_no:
        t = Ticket(10001, p1, train, seats)

        if t.book_ticket():
            t.display_ticket()
        break
else:
    print("Train not found!")
