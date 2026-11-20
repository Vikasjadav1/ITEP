'''
34. Cloud Storage Interface

Methods:

upload()
download()

Implement:

GoogleDrive
Dropbox
'''
from abc import ABC,abstractmethod
class Cloud_Storage(ABC):
    @abstractmethod
    def upload(self):
        pass
    @abstractmethod
    def download(self):
        pass

class GoogleDrive(Cloud_Storage):
    def upload(self):
        print("upload in google drive.....")
    
    def download(self):
        print("download from google drive ............")

class Dropbox(Cloud_Storage):
    def upload(self):
        print("upload in Dropbox drive.....")
    
    def download(self):
        print("download from Dropbox ............")

obj=GoogleDrive()
obj.upload()
obj.download()
print(".............")

obj=Dropbox()
obj.upload()
obj.download()
print(".............")

