'''
38. File Compression Tool

Methods:

compress()

Implement:

ZIPCompression
RARCompression
'''
from abc import ABC,abstractmethod
class File_Compression_Tool(ABC):
    @abstractmethod
    def compress(self):
        pass

class ZIPCompression(File_Compression_Tool):
    def compress(self):
        print("file compressed using ZIPCompression............")


class RARCompression(File_Compression_Tool):
    def compress(self):
        print("file compressed using RARCompression............")

obj=ZIPCompression()
obj.compress()
print("............................................")

obj=RARCompression()
obj.compress()