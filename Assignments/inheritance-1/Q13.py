'''
13. Smart Device System
Device
SmartDevice(Device)
SmartTV(SmartDevice)

Add WiFi support.
'''

class Device:
    def __init__(self, name, brand):
        self.__name = name
        self.__brand = brand

    def device_details(self):
        print("Device Name:", self.__name)
        print("Brand:", self.__brand)

class SmartDevice(Device):
    def __init__(self, name, brand, os):
        super().__init__(name, brand)
        self.__os = os

    def get_os(self):
        return self.__os

    def wifi_connect(self):
        print("WiFi Connected Successfully")

    def wifi_disconnect(self):
        print("WiFi Disconnected Successfully")        

class SmartTV(SmartDevice):
    def __init__(self, name, brand, os, size):
        super().__init__(name, brand, os)
        self.__size = size

    def tv_details(self):
        print("Operating System:", self.get_os())
        print("Screen Size:", self.__size)

    def play_video(self):
        print("Playing Video...")

    def change_channel(self):
        print("Channel Changed Successfully")


obj = SmartTV("Smart TV", "Samsung", "Android", 55)


obj.device_details()
obj.tv_details()


obj.wifi_connect()
obj.wifi_disconnect()


obj.play_video()
obj.change_channel()
