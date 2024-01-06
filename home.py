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
        db.collection("subject")
        .where(filter=FieldFilter(db.field_path(credent.email), "==", True))
        .stream()
    )
for doc in docs:
    st.markdown(f"""<h1 style="font-family: 'Kanit', sans-serif; color:#6896d4;">{doc.to_dict()["name"]}</h1>""",
                unsafe_allow_html=True)
    std = (
        db.collection("student")
        .where(filter=FieldFilter(db.field_path(doc.to_dict()["ID"]), "==", True))
        .stream()
    )
    for s in std:
        st.markdown(f"""<h5 style="font-family: 'Kanit', sans-serif; color:#a8c6f0;">{s.to_dict()["name"]} {s.to_dict()["surname"]}</h5>""",
                    unsafe_allow_html=True)
        #st.write(f"{s.to_dict()["name"]} {s.to_dict()["surname"]}")