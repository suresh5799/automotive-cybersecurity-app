import streamlit as st
import PyPDF2 as pdf
import os


upload="uploaded_file"
#upload="D:\OneDrive - LTTS\GUI\Client"

st.logo("images/auto2.jpg")

#Function to delete a file by name
def delete_file(filename):
    file_path=os.path.join(upload,filename)
    if os.path.exists(file_path):
        os.remove(file_path)
        return f"File '{filename}' has been deleted."
    else:
        return f"File '{filename}' not found."

#Get list of files in uploaded folder
def list_files():
    if os.path.exists(upload):
        return os.listdir(upload)
    else:
        []

st.header("Enter yout PS Number for Delete a files")

a=st.text_input("PS Number",key="ps_number")
user=["40037840","40037842","40037797","40036090"]

if a:
    if a in user:
        st.success("Authorized! You can Delete the file.")

        #Display the list of uploaded files
        st.write("## Files in the upload Folder")
        if os.path.exists(upload):
            files_in_folder=list_files()
            if files_in_folder:
                st.write("These are the Available files.")
                for file in files_in_folder:
                    st.write(file)

            else:
                st.write("No files uploaded yet.")


            #File deletion section
            st.write("## Delete a file")
            file_to_delete=st.text_input("Enter the filename to delete")

            if st.button("Delete File"):
                if file_to_delete:
                    result=delete_file(file_to_delete)
                    st.write(result)
                else:
                    st.warning("Please Enter a filename to delete.")
        else:
            st.warning("The floder does not exist yet. Please upload a file using Fileuploader Page.")
    else:
        st.error("Unauthorized! Only specific users can upload files.")

elif a:
    st.error("Please Enter Your PS Number to Proceed.")
