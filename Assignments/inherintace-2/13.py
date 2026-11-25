'''
13. File Export System
Problem Statement

Application exports files in multiple formats.

Create:

abstract class Exporter

Child:

PDFExporter
ExcelExporter
CSVExporter
'''
from abc import ABC, abstractmethod

class Exporter(ABC):

    @abstractmethod
    def export(self):
        pass


class PDFExporter(Exporter):

    def export(self):
        print("File exported successfully in PDF format.")


class ExcelExporter(Exporter):

    def export(self):
        print("File exported successfully in Excel format.")


class CSVExporter(Exporter):

    def export(self):
        print("File exported successfully in CSV format.")


print("Choose Export Format:")
print("1. PDF")
print("2. Excel")
print("3. CSV")

choice = int(input("Enter your choice: "))

if choice == 1:
    obj = PDFExporter()

elif choice == 2:
    obj = ExcelExporter()

elif choice == 3:
    obj = CSVExporter()

else:
    print("Invalid choice")
    obj = None

if obj:
    obj.export()