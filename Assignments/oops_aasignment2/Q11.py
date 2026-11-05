class Product:
    def __init__(self,name,price,category):
        self.name=name
        self.price=price
        self.category=category

    @staticmethod
    def apply_gst(price):
        gst=price*18/100
        return price+gst

    def apply_discount(self):
        if self.category=="Electronic":
            discount=self.price*10/100
        elif self.category=="clothing":
            discount=self.price*20/100
        elif self.category=="Food":
            discount=self.price*5/100
        else:
            discount=0

        return self.price-discount

    def display_price(self):
        discount_price=self.apply_discount()
        final_price=Product.apply_gst(discount_price)
        print(f"product : {self.name}")
        print(f"original price : {self.price}")
        print(f"after discount : {discount_price}")
        print(f"final price with gst : {final_price}")


p1=Product("laptop",50000,"Electronic")
p2=Product("shirt",500,"Cloth")
p3=Product("Rice",100,"Food")
p1.display_price()
p2.display_price()
p3.display_price()