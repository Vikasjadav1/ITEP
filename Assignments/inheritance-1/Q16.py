'''
16. E-commerce User Roles
User
Seller(User)
PremiumSeller(Seller)

Add premium benefits.
'''

class User:
    def __init__(self, name, email):
        self.__name = name
        self.__email = email

    def user_details(self):
        print("User Name:", self.__name)
        print("Email:", self.__email)

class Seller(User):
    def __init__(self, name, email, shop_name):
        super().__init__(name, email)
        self.__shop_name = shop_name

    def seller_details(self):
        print("Shop Name:", self.__shop_name)

class PremiumSeller(Seller):
    def __init__(self, name, email, shop_name):
        super().__init__(name, email, shop_name)

    def premium_benefits(self):
        print("Premium Seller Benefits:")
        print("1. 50% discount on commission.")
        print("2. Priority product listing.")
        print("3. Free shipping support.")
        print("4. Priority customer support.")

obj=PremiumSeller("vikas","viaskfiadsj","djn")
obj.user_details()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
obj.seller_details()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
obj.premium_benefits()