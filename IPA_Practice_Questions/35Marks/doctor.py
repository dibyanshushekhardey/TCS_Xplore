'''
Create a class Doctor with below attributes:
doctorId - Numeric type
doctorName - String type
specialization - String type
consultationFee - Numeric type

doctorId represents the unique identification number of a Doctor object.
doctorName represents the name of the doctor.
specialization represents the doctor specialization and 
consultationFee represents the doctors fee.

Define the __init__ method to initialize the attributes in the above sequence.

Create a class Hospital with below attribute:
doctorDB   - is of type dictionary with Doctor objects 
[Serial number of a Doctor in the Hospital and the respective Doctor object as a key : value pair ]

Define the __init__ method to initialize the dictionary attribute in the Hospital class . 
It initializes the dictionary of Doctor objects in the Hospital class with the dictionary 
supplied from main program while creating the Hospital object.

The Dictionary(with Doctor serial number and the respective Doctor object as key : value pair) 
is created and filled in main program by adding each Doctor object. This Doctor object is 
created with the input data related to a respective Doctor object . This dictionary after 
filling to be passed as an argument to the Hospital constructor and this will be initialized 
to doctorDB dictionary with in the Hospital class.

Define two methods - searchByDoctorName and calculateConsultationFeeBySpecialization in
Hospital class.

searchByDoctorName:
This method will take Doctor name as a parameter, find the respective Doctor object 
based on the doctor name given and return to main function with a list of Doctor objects, 
whose name matches with the given name, supplied as an argument.

If there is no Doctor found with the given name then return None to main program and 
display the message “No Doctor Exists with the given DoctorName” in the main function.

Hint:
a. Use the dictionary, doctorDB in Hospital object to find out the Doctor object(s) 
based on the given Doctor name.

b. Display the Doctor object /list of doctor objects (returned by this function) in 
the main function - Refer sample testcase below for more details


calculateConsultationFeeBySpecialization:
This method will take a Doctor specialization as parameter and return 
the total consultationFee of all the Doctors ,whose specialization is same 
as supplied as an argument from the main program. 

If there is no Doctor found with the given specialization then return 0 to main 
program and display the message “No Doctor with the given specialization” in the 
main function, excluding the double quotes

These two methods(described above) should be called from the main 
function / program and in the above order.

Hint

a. Use the dictionary, doctorDB in hospital to get the consultation fee of each 
of Doctor (Doctor object in the Hospital ) for the given specialization supplied as argument .

b.Display the Total Fee in the  in the main function  - Refer sample testcase
 below for more details

Instructions to implement Main function:

a. You would required to write the main program completely, hence please 
follow the below instructions for the same.

b. You would required to write the main program, inlign to the sample input 
data mentioned below and to read the same  .

c. Create the respective objects(Doctor and Hospital) 

  i.Create a Doctor object after reading the data related to one Doctor
   and add the doctor object to Doctors dictionary with Serial number and
    Doctor object as key:value pair.

  ii.Repeat above point for the total number of Doctor objects , read in 
  the first line of input data.

  iii. Create a Hospital Object with the dictionary of Doctor objects,
   created in the previous step (c.i)

d. Call the methods ( searchByDoctorName and calculateConsultationFeeBySpecialization) 
mentioned above in the same order , they appear in the question text from main function .

e. Display the data returned by the functions , in the main program as per the format 
mentioned in the sample output.

    If no Doctor exists with the given name(return value None from the respective 
    function )then display the message “No Doctor Exists with the given DoctorName” in the main
     function, excluding the double quotes.
    If no Doctor exists with the given specialization (return value 0 from the respective
     function )then display the message “No Doctor with the given specialization” in the main 
     function, excluding the double quotes.

Sample Input (below) data description:

1.The 1st input taken in the main section is the number of Doctor objects 
to be created and added to the dictionary of Doctors in the Main program

2.The next set of inputs are the doctorId, doctorName, specialization and 
consultationFee of first Doctor

3. For each Doctor object repeat point#2  and this point is repeated for
 number of Doctor objects given in the first line of input

4.The last but one line of input refers the doctorName to be searched  ie
 an argument for searchByDoctorName function

5. Last line of input represents the specialization, 
supplied as an argument to calculateConsultationFeeBySpecialization function, 
to get the total consultationFee of all the Doctors for a given specialization.

Sample Input :

5
90901
GovindRajulu
ENT
500
90902
Madhuri
Dermatologist
700
90903
Divya
Gynaecologist
600
90904
Suryam
Cardiologist
900
90905
Madhuri
Cardiologist
1000
Madhuri
Cardiologist

Output :

90902
Madhuri
Dermatologist
700
90905
Madhuri
Cardiologist
1000
1900


'''

# class Doctor:
#     def __init__(self, doctorId, doctorName, specialization, consultationFee):
#         self.doctorId=doctorId
#         self.doctorName = doctorName
#         self.specialization=specialization
#         self.consultationFee=consultationFee

# class Hospital:
#     def __init__(self, doctor_dict):
#         self.doctor_dict=doctor_dict
    
#     def searchBydoctorName(self, inpt_dname):
#         lst=[]
#         for k, v in self.doctor_dict.items():
#             if v.doctorName.lower() == inpt_dname.lower():
#                 lst.append(v)
        
#         if lst == []:
#             print('No Doctor Exists with the given DoctorName')
#         else:
#             for i in lst:
#                 print(i.doctorId)
#                 print(i.doctorName)
#                 print(i.specialization)
#                 print(i.consultationFee)
    
#     def calculateConsulationFeeBySpecialization(self, inpt_sp):
#         fee = 0
#         for k, v in self.doctor_dict.items():
#             if v.specialization.lower() == inpt_sp.lower():
#                 fee += v.consultationFee
#         if fee == 0:
#             print('No Doctor with the given specialization')
#         else:
#             print(fee)


# n=int(input())
# doctor_dict={}
# sno=1
# for i in range(n):
#     doctorId=int(input())
#     doctorName=input()
#     specialization=input()
#     consultationFee=int(input())
#     doctor_dict[sno]=Doctor(doctorId, doctorName, specialization, consultationFee)
#     sno += 1
# inpt_dname=input()
# inpt_sp=input()
# obj=Hospital(doctor_dict)
# obj.searchBydoctorName(inpt_dname)
# obj.calculateConsulationFeeBySpecialization(inpt_sp)

class Doctor:
    def __init__(self, doctorId, doctorName, specialization, consultationFee):
        self.doctorId=doctorId
        self.doctorName = doctorName
        self.specialization=specialization
        self.consultationFee=consultationFee

class Hospital:
    
    @staticmethod
    def searchBydoctorName(doctor_dict, inpt_dname):
        lst=[]
        for k, v in doctor_dict.items():
            if v.doctorName.lower() == inpt_dname.lower():
                lst.append(v)
        
        if lst == []:
            print('No Doctor Exists with the given DoctorName')
        else:
            for i in lst:
                print(i.doctorId)
                print(i.doctorName)
                print(i.specialization)
                print(i.consultationFee)
    
    @staticmethod
    def calculateConsulationFeeBySpecialization(doctor_dict, inpt_sp):
        fee = 0
        for k, v in doctor_dict.items():
            if v.specialization.lower() == inpt_sp.lower():
                fee += v.consultationFee
        if fee == 0:
            print('No Doctor with the given specialization')
        else:
            print(fee)


n=int(input())
doctor_dict={}
sno=1
for i in range(n):
    doctorId=int(input())
    doctorName=input()
    specialization=input()
    consultationFee=int(input())
    doctor_dict[sno]=Doctor(doctorId, doctorName, specialization, consultationFee)
    sno += 1
inpt_dname=input()
inpt_sp=input()
#obj=Hospital(doctor_dict)
Hospital.searchBydoctorName(doctor_dict,inpt_dname)
Hospital.calculateConsulationFeeBySpecialization(doctor_dict,inpt_sp)