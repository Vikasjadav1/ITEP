from abc import ABC,abstractmethod
class HospitalStaff(ABC):
    @abstractmethod
    def dutie(self):
        pass

class Doctor(HospitalStaff):
    def dutie(self):
        print("Doctor's Responsibilities:")
        print("1. Check patients and diagnose diseases.")
        print("2. Prescribe medicines.")
        print("3. Perform surgeries and treatments.")
        print("4. Monitor patients' health.")
        print("5. Provide medical advice.")

class Nurse(HospitalStaff):
    def dutie(self):
        print("Nurse's Responsibilities:")
        print("1. Take care of patients.")
        print("2. Give medicines and injections.")
        print("3. Check blood pressure and temperature.")
        print("4. Follow doctor's instructions.")
        print("5. Maintain patient health records.")


class Receptionist(HospitalStaff):
    def dutie(self):
        print("Receptionist's Responsibilities:")
        print("1. Register new patients.")
        print("2. Book appointments.")
        print("3. Manage patient records.")
        print("4. Handle phone calls.")
        print("5. Manage billing and payments.")

obj=Doctor()
obj.dutie()

print("*************************************")

obj=Nurse()
obj.dutie()

print("*************************************")

obj=Receptionist()
obj.dutie()

print("*************************************")