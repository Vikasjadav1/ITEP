'''
19. Mobile Phone Hierarchy
Phone
Smartphone
AndroidPhone

Add Android features.
'''

class Phone:
    def phone(self):
        print("its normal phone......")
    
class Smartphone(Phone):
    def smartphone(self):
        print("its smart phone...")

class AndroidPhone(Smartphone):
    def androidphone(self):
        print("Android Features:")
        print("1. Touchscreen Display.")
        print("2. WiFi and Bluetooth Connectivity.")
        print("3. Google Play Store Support.")


obj=AndroidPhone()
obj.phone()
obj.smartphone()
obj.androidphone()


