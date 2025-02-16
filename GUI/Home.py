import streamlit as st
import os
import PyPDF2 as pdf
import pandas as pd
import math


upload ="uploaded_file"
#os.makedirs(upload, exist_ok=True)
st.set_page_config(page_title="cybersecurity",page_icon="🔐",)
st.sidebar.success("select a page above")

def extract_text_from_pdf(file_path,goal_name):
        results={}
        #for file in os.listdir(upload):
        if file.endswith(".pdf"):
            #file path = os.path.join(upload, file)
            with open(file_path, "rb") as pdf_file:reader = pdf.pdfReader(pdf_file)
            text=""

            # Extract text from all pages
            for page in reader.pages:
                text += page.extract_text()+ "\n"

            # Search for the goal name
            if goal_name.lower() in text.lower():
                start_index = text.lower().find(goal_name,lower())    # Find goal name
                #print(start_index)

                # Extract from goal onward
                extracted_text = text[start_index:]
                lines = extracted_text.splitlines()

                #Step 2: select the first line
                first_line = lines[0]
                a=first_line.lower()
                b=a.replace("  ","")
                #print(f"{b,goal_name}")
                t=o
                if goal_name == b:
                    l=[]
                    c=O
                    # Extract only the requirements (until next goal starts)
                    for line in extracted_text.splitlines():
                        if line.strip()=="":
                            c=c+1 
                        elif c==2:
                            break
                        else:
                            l.append(line)
                    #All the requirements and goal name are prestent in the l list[]
                    results[file] =l

                    return results

                else:
                    #if goal_name!=b:
                    t=t+1

error=[]

# Search Functionality
st.subheader("Search for Requirements by Goal Name")

#Here asking a goal name to user
goal_name = st.text_input("Enter Goal Name (e.g., Secure Authenticatio or secure flash)")

if st.button("Search"):
    if goal_name:
        if upload:
            
            for file in os.listdir(upload):
            #if file:
                file_path = os.path.join(upload,file)
                pdf_text = extract_text_from_pdf(file_path,goal_name)
                if pdf_text:
                    for file,text in pdf_text.items():
                        st.write(f"### Results from: {file}")
                        #st.write(text)
                        for a in text:
                            st.write(a)
                else:
                    error.append(file)
                    #st.warning(f"No matching goal found in this:{file}")
            #else:
               # st.error("Kindly Upload a File before initiating the search")

            for a in error:
                st.error(f"No matching goal'found in this file:{a}")

        else:
            st.error("Kindly Upload a File before initiating the search")

    else:
        st.error("First Enter the Goal Name")


