'''
32. Database Interface

Methods:

connect()
disconnect()

Implement:

MySQL
MongoDB
PostgreSQL
'''
from abc import ABC,abstractmethod
class Database(ABC):
    @abstractmethod
    def connect(self):
        pass
    @abstractmethod
    def disconnect(self):
        pass

class MySQL(Database):
    def connect(self):
        print("mySQl connect....")
    
    def disconnect(self):
        print("mySQL disconnect")

class MongoDB(Database):
    def connect(self):
        print("MongoDB connect....")
    
    def disconnect(self):
        print("MongoDB disconnect")

class PostgreSQL(Database):
    def connect(self):
        print("PostgreSQL connect....")
    
    def disconnect(self):
        print("PostgreSQL disconnect")

obj=MySQL()
obj.connect()
obj.disconnect()
print(".............")

obj=MongoDB()
obj.connect()
obj.disconnect()
print(".............")

obj=PostgreSQL()
obj.connect()
obj.disconnect()
print(".............")