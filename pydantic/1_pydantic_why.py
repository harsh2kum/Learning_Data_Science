# from pydantic import BaseModel, EmailStr, AnyUrl, Field
# from typing import List, Dict, Optional, Annotated

# class Patient(BaseModel):

#     name: Annotated[str, Field(max_length=50, title='Name of the patient', description='Give the name of the patient in less than 50 chars', examples=['Nitish', 'Amit'])]
#     email: EmailStr
#     linkedin_url: AnyUrl
#     age: int = Field(gt=0, lt=120)
#     weight: Annotated[float, Field(gt=0, strict=True)]
#     married: Annotated[bool, Field(default=None, description='Is the patient married or not')]
#     allergies: Annotated[Optional[List[str]], Field(default=None, max_items=5)]   # FIXED
#     contact_details: Dict[str, str]


# def update_patient_data(patient: Patient):

#     print(patient.name)
#     print(patient.age)
#     print(patient.allergies)
#     print(patient.married)
#     print('updated')

# patient_info = {
#     'name':'nitish',
#     'email':'abc@gmail.com',
#     'linkedin_url':'http://linkedin.com/1322',
#     'age': '30',
#     'weight': 75.2,
#     'contact_details': {'phone':'2353462'}
# }

# patient1 = Patient(**patient_info)

# update_patient_data(patient1)


##copilot
from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name: Annotated[
        str,
        Field(
            max_length=50,
            title='Name of the patient',
            description='Give the name of the patient in less than 50 chars',
            examples=['Nitish', 'Amit']
        )
    ]
    email: EmailStr
    linkedin_url: AnyUrl
    age: int = Field(gt=0, lt=120)
    weight: Annotated[float, Field(gt=0, strict=True)]
    married: Annotated[Optional[bool], Field(default=None, description='Is the patient married or not')]
    allergies: Annotated[Optional[List[str]], Field(default=None, max_length=5)]  # ✅ fixed for Pydantic v2
    contact_details: Dict[str, str]

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print('updated')

# Example input
patient_info = {
    'name': 'Harsh',
    'email': 'abc@gmail.com',
    'linkedin_url': 'http://linkedin.com/1322',
    'age': 25,  # ✅ int instead of string
    'weight': 75.2,
    'married': True,
    'allergies': ['pollen', 'dust'],
    'contact_details': {'phone': '2353462'}
}

patient1 = Patient(**patient_info)
update_patient_data(patient1)
