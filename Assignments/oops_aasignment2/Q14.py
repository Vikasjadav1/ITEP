class Restaurant:
    def __init__(self,table_no):
        self.table_no=table_no
        self.ordered_items=[]
        self.prices=[]

    def add_item(self,item,price):
        if item not in self.ordered_items:
            self.ordered_items.append(item)
            self.prices.append(price)
            print("ordered successfully....")
        else:
            print(f"{item} already ordered......")

    def remove_item(self,item):
        if item in self.ordered_items:
            index=self.ordered_items.index(item)
            self.ordered_items.pop(index)
            self.prices.pop(index)
            print(f"{item} removed successfully")
        else:
            print(f"{item} not found")
    
    def total_bill(self):
        bill=0
        for price in self.prices:
            bill+=price
        return bill

    def display(self,bill,final_bill):
        print(f"order items : {self.ordered_items}")
        print(f"prices : {self.prices}")
        print(f"bill : {bill}")
        print(f"final bill after tax : {final_bill}")

    @staticmethod
    def tax(bill):
        tax=bill*18/100
        return bill+tax 


ord1=Restaurant(101)
ord1.add_item("pizza",100)
ord1.add_item("burger",100)
ord1.add_item("pasta",100)

ord1.remove_item("pizza")
bill=ord1.total_bill()
final_bill=Restaurant.tax(bill)

ord1.display(bill,final_bill)
