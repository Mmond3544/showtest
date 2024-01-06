import firebase_admin
import streamlit as st
from firebase_admin import credentials
from firebase_admin import firestore
from google.cloud.firestore_v1 import FieldFilter
import credent
try:
    cred = credentials.Certificate("cert.json")
    firebase_admin.initialize_app(cred)
except ValueError as e:
    app = firebase_admin.get_app()

db = firestore.client()

docs = (
    db.collection("test")
    .where(filter=FieldFilter("Teacher", "==", credent.email))
    .stream()
)
for doc in docs:
    dataID = db.collection("test").document(doc.id)
    data = dataID.get()
    if doc.exists:
        st.subheader(doc.id)
        st.write(doc.to_dict())
        #if st.button(key=ID,label="Delete"):
            #db.collection("student").document(ID).delete()
        st.subheader("",divider='rainbow')
    else:
        st.write('No such document!')
