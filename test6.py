### ref:  https://towardsdatascience.com/how-to-add-a-user-authentication-service-in-streamlit-a8b93bf02031

import streamlit as st
import streamlit_authenticator as stauth
import pandas as pd
import numpy as np
import csv

st.title("Dexcom Students System")
######### Global variables  ##########
names = ['Admin','Teacher']
usernames = ['admin','teacher']
passwords = ['123','456']

Button = ["Add Admin","Add Teacher","Add Student"]
##################################
hashed_passwords = stauth.Hasher(passwords).generate()
authenticator = stauth.Authenticate(names,usernames,hashed_passwords,
    'some_cookie_name','some_signature_key',cookie_expiry_days=30)

name, authentication_status, username = authenticator.login('Login','main')


if authentication_status:
    authenticator.logout('Logout', 'main')
    st.write('## Welcome *%s*' % (name))
    st.button(Button[0])
    st.button(Button[1])
    st.button(Button[2])
    if st.button(Button[0]):  ### add admin
        pass
    elif st.button(Button[1]):  ### add teacher
        pass
    elif st.button(Button[2]):  ### add student
        file1 = open("student_data.csv")
        df_students = pd.DataFrame(file1)  
        file1.close()
        
        student_id = st.sidebar.text_input("Student ID")
        student_name = st.sidebar.text_input("Student Name")
        student_phone = st.sidebar.text_input("Student Phone Number")
        student_email = st.sidebar.text_input("Student Email")
        student_class_name = st.sidebar.text_input("Student Class Name")
        student_subject = st.sidebar.text_input("Student Subject")
        
        @st.cache(allow_output_mutation=True)
        def get_data():
            return []
            
        
        df_students = pd.DataFrame(get_data())
        st.write("## Show Dataset")
        st.write(df_students)
        st.write(df_students.shape)
        if st.button("Add Student"):
            get_data().append({"Student_ID": student_id, 
                           "Student_Name": student_name, 
                           "Student_Phone": student_phone,
                           "Student_Email": student_email,
                           "Student_Class_Name": student_class_name,
                           "Student_Subject": student_subject})
        
#####convert df to csv and save it    ###
        def convert_df(df_students):
            return df_students.to_csv().encode('utf-8')
        
        
        csv1 = convert_df(df_students)
        #st.write(csv1)
        
        file2 = open('student_data.csv')
        df_students.to_csv (r'student_data.csv', index = False, header=True)
        file2.close()

elif authentication_status == False:
    st.error('Username/password is incorrect')
elif authentication_status == None:
    st.warning('Please enter your username and password')
