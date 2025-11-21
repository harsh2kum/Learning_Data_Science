# Pydantic is a Python library used to validate data and convert (parse) it into the correct format automatically.
# It is widely used in FastAPI, but you can use it in any Python project.

# def insert_patient_data(name: str,age:int):
#     if type(name) == str and type(age) == int:
#         if age < 0:
#             raise ValueError('Age cant be negative')
#         else:
#             print(name)
#             print(age)
#             print('inserted into database') 
#     else:
#         raise TypeError('Incorrect data type')
    
# insert_patient_data('harsh',34)


from pydantic import BaseModel

class Patient(BaseModel):
    
    name: str
    age: int 

def insert_patient_data(patient:Patient):
    
    print(patient.name)
    print(patient.age)
    print('innserted')
    
def update_patient_data(patient: Patient):
    
    print(patient.name)
    print(patient.age)
    print('update')   
#create a dictionary 
patient_info = {'name':"Harsh",'age':30}

patient1 = Patient(**patient_info)  # ** is used to unpack dictionary 

#call the function 
insert_patient_data(patient1)

update_patient_data(patient1)


