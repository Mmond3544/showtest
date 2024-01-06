import firebase_admin
import streamlit as st
from firebase_admin import credentials
from firebase_admin import firestore
#from st_pages import Page, show_pages
from streamlit_extras.switch_page_button import switch_page
try:
    cred = credentials.Certificate("cert.json")
    firebase_admin.initialize_app(cred)
except ValueError as e:
    app = firebase_admin.get_app()

db = firestore.client()

docs = (
    db.collection("student").stream()
)
#show_pages([Page("student.py", "Student")])

placeholder = st.empty()
with placeholder.form("Add"):
    ID = st.text_input("Student ID")
    Name = st.text_input("Name")
    Surname = st.text_input("Surname")
    submit = st.form_submit_button("Add Student")
    if submit:
        stdName = {"name": Name, "surname": Surname}
        db.collection("student").document(ID).set(stdName)
        st.toast('Add Success')
#if st.button('Cancel'):
    #switch_page(show_pages([Page("student.py")]))

