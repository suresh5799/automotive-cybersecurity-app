import streamlit as st
import PyPDF2 as pdf
import os




#it willcreate a folder for storing a files
upload = "uploaded_file"
os.makedirs(upload, exist_ok=True)

#title
st.title("Enter your ps Number for Uploding pdf")

a=st.text_input("Ps Number",key="ps_number")

if a=="40037840" or a=="40037842" or a=="40037797":
    st.success("Authorized! You can upload files.")

    #file uploaded into uploadede_file folder
    uploaded_file = st.file_uploader("Upload PDF", type='pdf')

    if uploaded_file:
        file_path = os.path.join(upload, uploaded_file.name)

        with open(file_path,"wb") as f:
            f.write(uploaded_file.getbuffer())
            st.session_stats["uploaded_file"]=uploaded_file
            st.success(f"File uploaded successfully: {uploaded_file.name}")

else:
    st.error("Unauthorized! Only specific users can upload files.")


