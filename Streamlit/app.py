import streamlit as st
import requests

#give the fast api url
BASE_URL = "http://127.0.0.1:8000"

st_title('Student Management system ')

menu = ['Create student','View all the student','get students by ID','Update student info','Delete student']

choice = st.sidebar.selectbox('Menu',menu)


#create students 
if choice == 'create student':
    st.header('Create Student')
    name = st.text_input('Student name ')
    email = st.text_input('students')
    course = st.text_input('Enter course')
    if st.buttom('Create new student'):
        data = {
            'name':name,
            'email':email,
            'course':course
        }
        response = response.post(url:f'{BASE_URL}/students/',json=data)
        
        if response.status_code == 200:
            st.success('student created successfully =')