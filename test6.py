# -*- coding: utf-8 -*-
"""
Created on Thu May 12 09:27:11 2022

@author: Gamal
"""
### ref:  https://towardsdatascience.com/how-to-add-a-user-authentication-service-in-streamlit-a8b93bf02031

import streamlit as st
import streamlit_authenticator as stauth
import pandas as pd
import numpy as np
import csv

st.title("Dexcom Student System")
######### Global variables  ##########
names = ['Admin','Teacher']
usernames = ['admin','teacher']
passwords = ['123','456']
##################################
hashed_passwords = stauth.Hasher(passwords).generate()
authenticator = stauth.Authenticate(names,usernames,hashed_passwords,
    'some_cookie_name','some_signature_key',cookie_expiry_days=30)

name, authentication_status, username = authenticator.login('Login','main')


if authentication_status:
    authenticator.logout('Logout', 'main')
    st.write('## Welcome *%s*' % (name))
    st.write("## Show Pervious Data")
    file1 = open("student_data.csv")
    df_students = pd.DataFrame(file1)   #pd.read_csv("student_data.csv")
    st.write(df_students)
    st.write(df_students.shape)
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


##reading_value = st.sidebar.number_input('The reading from Dexcom sensor')


    if st.button("Add Student"):
        get_data().append({"Student_ID": student_id, 
                       "Student_Name": student_name, 
                       "Student_Phone": student_phone,
                       "Student_Email": student_email,
                       "Student_Class_Name": student_class_name,
                       "Student_Subject": student_subject})

    df_students = pd.DataFrame(get_data())
    st.write("## Show New Data")
    st.write(df_students)
    st.write(df_students.shape)

### convert df to csv and save it    ###
    def convert_df(df_students):
        return df_students.to_csv().encode('utf-8')


    csv1 = convert_df(df_students)
    st.write(csv1)

    file2 = open('student_data.csv')
    df_students.to_csv (r'student_data.csv', index = False, header=True)
    file2.close()

elif authentication_status == False:
    st.error('Username/password is incorrect')
elif authentication_status == None:
    st.warning('Please enter your username and password')
    
# if st.session_state['authentication_status']:
#     authenticator.logout('Logout', 'main')
#     st.write('Welcome *%s*' % (st.session_state['name']))
    
# elif st.session_state['authentication_status'] == False:
#     st.error('Username/password is incorrect')
# elif st.session_state['authentication_status'] == None:
#     st.warning('Please enter your username and password')

######################

# select = st.selectbox('Select', ('About', 'Login'), 0)

# username = st.text_input("Username")
# password = st.text_input("password")
# if select == 'About':
#     st.info('This system to enter student ,Class, subjects')
# else :
#     st.write("## Login")
#     if username == "admin" and password == "admin" :
#         st.empty(select)

#button = st.button('button')
# if button == 1 :
#     page = 'Plot'  # does not work

# st.write("# test")
# with st.empty():
#     box = st.number_input("enter number")
#     time.sleep(10)
#     if box == 1 :
#         st.empty()
#     else:
#         st.write("The pass wrong")
        
    



# placeholder = st.empty()

# # Replace the placeholder with some text:
# placeholder.text("Hello")

# # Replace the text with a chart:
# placeholder.line_chart({"data": [1, 5, 2, 6]})

# # Replace the chart with several elements:
# with placeholder.container():
#      st.write("This is one element")
#      st.write("This is another")

# # Clear all those elements:
# placeholder.empty()




# import time

# with st.empty():
#      for seconds in range(60):
#          st.write(f"⏳ {seconds} seconds have passed")
#          time.sleep(1)
#      st.write("✔️ 1 minute over!")