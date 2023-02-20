# doctor class
class Doctor:
    doctors = []
    def __init__(self, doctor_name, doctor_specialisation, doctor_fee):
        self.doctor_name = doctor_name
        self.doctor_specialisation=doctor_specialisation
        self.doctor_fee = doctor_fee
    
    def __str__(self):
        return self.doctor_name+'\t'+self.doctor_specialisation+'\t'+str(self.doctor_fee)
    @classmethod
    def create_doctors(cls):
        with open('doctors_list.txt', 'r+') as doctor:
            d=doctor.readlines()
            for i in d:
                j=i.split('|')
                obj=Doctor(j[0], j[1], j[2])
                Doctor.doctors.append(obj)

if __name__=="__main__":
    Doctor.create_doctors()
    for i in Doctor.doctors:
        print(i)