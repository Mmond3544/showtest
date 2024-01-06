import firebase_admin
import streamlit as st
from firebase_admin import credentials
from firebase_admin import firestore
from google.cloud.firestore_v1 import FieldFilter
from st_pages import Page, show_pages, add_page_title
try:
    cred = credentials.Certificate("cert.json")
    firebase_admin.initialize_app(cred)
except ValueError as e:
    app = firebase_admin.get_app()

db = firestore.client()

docs = (
    db.collection("student").stream()
)

#def open():
    #show_pages([Page("addstd.py", "add")])

#if st.button("Add"):
    #switch_page("addstd.py")
#if st.sidebar.button("Add"):
    #open()
for doc in docs:
    dataID = db.collection("student").document(doc.id)
    data = dataID.get()
    if doc.exists:
        ID = str(doc.id)
        name = str(doc.to_dict()['name'])
        surname = str(doc.to_dict()['surname'])
        show = ID+" "+name+" "+surname
        st.subheader(show)
        #if st.button(key=ID,label="Delete"):
            #db.collection("student").document(ID).delete()
        st.subheader("",divider='rainbow')
    else:
        st.write('No such document!')