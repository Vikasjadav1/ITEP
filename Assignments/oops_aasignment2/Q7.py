class Patient:
    __patient_count=0
    def __init__(self,patient_id,name,disease,doctor_assigned):
        self.__patient_id=patient_id
        self.__name=name
        self.__disease=disease
        self.__doctor_assigned=doctor_assigned
        Patient.__patient_count+=1

    def display(self):
        print(f"patient id : {self.__patient_id}")
        print(f"patient name : {self.__name}")
        print(f"disease : {self.__disease}")
        print(f"doctor assined : {self.__doctor_assigned}")

    def change_doctor(self,doctor):
        if self.__doctor_assigned==doctor:
            print(f"already you have assigned this dcotor ....")
        else:
            self.__doctor_assigned=doctor
            print(f"doctor changed.....")

    @classmethod
    def get_data(cls,data):
        id,name,disease,doctor =  data.split("-")
        return cls(id,name,disease,doctor)

    @classmethod
    def patient_count(cls):
        return cls.__patient_count

    
patient1=Patient.get_data("101-jp-fever-gupja ji")
patient2=Patient.get_data("102-kp-fever-gupja ji")
patient1.change_doctor("sharma ji")
patient1.display()
print(f"total patient {Patient.patient_count()}")
