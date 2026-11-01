'''
 Write a Java program to create a class with methods to search for flights and hotels, and to book and cancel reservations.
 '''

class TravelBooking:
    def __init__(self):
        self.flights = ["Indigo", "Air India", "SpiceJet"]
        self.hotels = ["Taj Hotel", "Radisson", "Marriott"]
        self.reservations = []    

    def search_flights(self):
        print("........ Available Flights ........")
        for i in range(len(self.flights)):
            print(f"{i+1}. {self.flights[i]}")

    def search_hotels(self):
        print("........ Available Hotels ........")
        for i in range(len(self.hotels)):
            print(f"{i+1}. {self.hotels[i]}")

    def book_reservation(self, item):
        if item in self.flights or item in self.hotels:
            if item not in self.reservations:
                self.reservations.append(item)
                print(f"{item} booked successfully!")
            else:
                print(f"{item} is already booked!")
        else:
            print(f"{item} is not available!")

    def cancel_reservation(self, item):
        if item in self.reservations:
            self.reservations.remove(item)
            print(f"{item} booking cancelled successfully!")
        else:
            print(f"No booking found for {item}")

    def show_reservations(self):
        print("........ Your Reservations ........")
        if len(self.reservations) == 0:
            print("No reservations found!")
        else:
            for item in self.reservations:
                print(item)

obj = TravelBooking()

obj.search_flights()
obj.search_hotels()
obj.book_reservation("Indigo")
obj.book_reservation("Taj Hotel")
obj.show_reservations()
obj.cancel_reservation("Indigo")
