class Airline:
    def __init__(self,flight_num,total_seat,booked_seat):
        self.flight_num=flight_num
        self.total_seat=total_seat
        self.booked_seat=booked_seat

    def book_flight(self,seat):
        reamaining_seat=self.total_seat-self.booked_seat
        if reamaining_seat==0:
            print("seats are not available.......")
        elif reamaining_seat>=seat:
            self.total_seat-=seat
            self.booked_seat+=seat
            print(f"flight booked for {seat} seats")
        else:
            print(f"booking cancelled......")

    def cancel(self,seat):
        self.total_seat+=seat
        self.booked_seat-=seat
        print("flight canceled........")



obj=Airline(15555,150,149)
obj.book_flight(1)
obj.cancel(1)
obj.book_flight(1)
obj.book_flight(1)
