'''
46. Hotel Booking System

Implement:

room types
booking
pricing
'''
class RoomType:
    def __init__(self):
        self.__single_room = 1000
        self.__double_room = 2000
        self.__deluxe_room = 3000
        self.__suite_room = 5000

        self.__single_available = 5
        self.__double_available = 3
        self.__deluxe_available = 2
        self.__suite_available = 1

    def get_single_room(self):
        return self.__single_room

    def get_double_room(self):
        return self.__double_room

    def get_deluxe_room(self):
        return self.__deluxe_room

    def get_suite_room(self):
        return self.__suite_room

    def get_single_available(self):
        return self.__single_available

    def get_double_available(self):
        return self.__double_available

    def get_deluxe_available(self):
        return self.__deluxe_available

    def get_suite_available(self):
        return self.__suite_available

    def available_room(self):
        print("\n----- Available Rooms -----")
        print(f"Single Room: Price {self.get_single_room()} | Available {self.get_single_available()}")
        print(f"Double Room: Price {self.get_double_room()} | Available {self.get_double_available()}")
        print(f"Deluxe Room: Price {self.get_deluxe_room()} | Available {self.get_deluxe_available()}")
        print(f"Suite Room: Price {self.get_suite_room()} | Available {self.get_suite_available()}")


class Booking(RoomType):
    def __init__(self, name, room, days):
        super().__init__()
        self.name = name
        self.room = room
        self.days = days
        self.total_price = 0

    def book_room(self):
        if self.room == "single":
            if self.get_single_available() > 0:
                self._RoomType__single_available -= 1
                self.total_price = self.get_single_room() * self.days

            else:
                print("Single room not available")

        elif self.room == "double":
            if self.get_double_available() > 0:
                self._RoomType__double_available -= 1
                self.total_price = self.get_double_room() * self.days

            else:
                print("Double room not available")

        elif self.room == "deluxe":
            if self.get_deluxe_available() > 0:
                self._RoomType__deluxe_available -= 1
                self.total_price = self.get_deluxe_room() * self.days

            else:
                print("Deluxe room not available")

        elif self.room == "suite":
            if self.get_suite_available() > 0:
                self._RoomType__suite_available -= 1
                self.total_price = self.get_suite_room() * self.days

            else:
                print("Suite room not available")

        else:
            print("Invalid room type")
            return

        if self.total_price > 0:
            print("\nRoom booked successfully!")

    def display_booking(self):
        if self.total_price > 0:
            print("\n----- Booking Details -----")
            print("Customer Name:", self.name)
            print("Room Type:", self.room)
            print("Days:", self.days)
            print("Total Price:", self.total_price)


rooms = RoomType()
rooms.available_room()

name = input("\nEnter customer name: ")
room = input("Enter room type (single/double/deluxe/suite): ").lower()
days = int(input("Enter number of days: "))

booking = Booking(name, room, days)
booking.book_room()
booking.display_booking()
