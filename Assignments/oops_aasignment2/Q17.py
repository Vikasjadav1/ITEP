class Bill:
    def __init__(self,consumer_id,units,):
        self.__consumer_id=consumer_id
        self.__units=units

    def cal_bill(self):
        if self.__units<=100:
            bill=self.__units*3
        elif self.__units<=200:
            bill=(100*3)+(self.__units-100)*5
        else:
            bill=(100*3)+(100*5)+(self.__units-200)*8
        return bill
    
    @staticmethod
    def add_surcharge(amount):
        surcharge=amount*10/100
        return amount+surcharge

    def display(self):
        bill=self.cal_bill()
        final_bill=self.add_surcharge(bill)

        print(f"consumer id : {self.__consumer_id}")
        print(f"units consumed : {self.__units}")
        print(f"electricity bill : {bill}")
        print(f"final bill with surcharge : {final_bill}")


consumer=Bill(1144,500)
consumer.display()
    

    
