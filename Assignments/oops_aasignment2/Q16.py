class Train:
    def __init__(self,train_num,total_seat,booked_seat):
        self.__train_num=train_num
        self.__total_seat=total_seat
        self.__booked_seat=booked_seat

    def reserve_seat(self,seat):
        reamaning_seat=self.__total_seat-self.__booked_seat
        if reamaning_seat==0:
            print("no seat available....")
        elif reamaning_seat>=seat:
            self.__total_seat-=seat
            self.__booked_seat+=seat
            print("seat booked successfully.......")
        else:
            print(f"booking cancelled... {reamaning_seat} seats are reamaning")
    
    def display_avialable_seat(self):
        reamaning_seat=self.__total_seat-self.__booked_seat
        print(f"{reamaning_seat} seats are reamaning")

obj=Train(111,30,25)
obj.display_avialable_seat()
obj.reserve_seat(5)