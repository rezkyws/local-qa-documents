# Second
import streamlit as st
import requests
# import anthropic


st.sidebar.success("Select Any Page from here")

st.title("📝 Upload Documents to Database") 

uploaded_files = st.file_uploader("Select your docs", type=("pdf"), accept_multiple_files=True) 

if uploaded_files:
    docs = []
    for uploaded_file in uploaded_files:
        # # read as bytes
        # print(uploaded_file.read())
        # # multiple files format
        # [('file', open('report.xls', 'rb')), ('file', open('report2.xls', 'rb'))]
        docs.append(('files', uploaded_file))

    with st.spinner('Vectorizing your docs is on progress...'):
        response = requests.post(
            'http://localhost:3347/api/v1/upload-docs', 
            files=docs, 
            timeout=300).json()

    st.success(response["message"])