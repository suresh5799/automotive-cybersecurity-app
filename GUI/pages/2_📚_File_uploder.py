import streamlit as st
import PyPDF2 as pdf
import os





#it willcreate a folder for storing a files
upload = "uploaded_file"
os.makedirs(upload, exist_ok=True)

st.logo("images/auto2.jpg")

#Function to check if a file with the same name exists
def file_exists(filename):
    return os.path.exists(os.path.join(upload,filename))

#title
st.header("Enter your ps Number for Uploding pdf")
#st.header("Enter your PS Number for Search.")

a=st.text_input("PS Number",key="ps_number")
user=["40037840","40037842","40037797"]

#a=st.text_input("Ps Number",key="ps_number")

#if a=="40037840" or a=="40037842" or a=="40037797":
if a:
    if a in user:
        st.success("Authorized! You can upload files.")

        #file uploaded into uploaded_file folder
        uploaded_file = st.file_uploader("Upload PDF", type='pdf')

        if uploaded_file:
            
            file_path = os.path.join(upload, uploaded_file.name)
            if file_exists(uploaded_file.name):
                st.error(f"A file with the name '{uploaded_file.name}' already exists. Please rename or check the file.")
            else:
                with open(file_path,"wb") as f:
                    f.write(uploaded_file.getbuffer())
                    st.session_state["uploaded_file"]=uploaded_file
                st.success(f"File uploaded successfully: {uploaded_file.name}")
                

    else:
        st.error("Unauthorized! Only specific users can upload files.")

elif a:
    st.error("Please Enter Your PS Number to Proceed.")


