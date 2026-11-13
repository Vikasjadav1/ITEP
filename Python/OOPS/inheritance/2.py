class J5:
    def recieving_call(self):
        print("call recieved.....")
    def rejecting_call(self):
        print("call rejected......")

class J7(J05):
    def camera(self):
        print("camera is on....")

j7=J7()
j7.receiving_call()
j7.rejecting_call()
j7.camera()     
