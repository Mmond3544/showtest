import firebase_admin
import self as self
from firebase_admin import credentials
from firebase_admin import firestore
from google.cloud.firestore_v1 import FieldFilter
try:
    cred = credentials.Certificate("cert.json")
    firebase_admin.initialize_app(cred)
except ValueError as e:
    app = firebase_admin.get_app()

db = firestore.client()
docs = db.collection("test").document(db.field_path("ST2022101-61")).get()
if docs is not None:
    db.collection("test").document("ST2023319-61").update(docs.to_dict())

