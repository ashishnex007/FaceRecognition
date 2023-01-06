
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://face-attendance-92581-default-rtdb.firebaseio.com/"
})

ref = db.reference('student')

data = {
    "C0":
        {
            "name" : "Rithvik",
            "ID" : "C0",
            "Dept" : "CSE",
            "year" : 2,
            "last_attendance" : "6-1-2023 09:00:00"
        },
    "C7":
        {
            "name" : "Ashish",
            "ID" : "C7",
            "Dept" : "CSE",
            "year" : 2,
            "last_attendance" : "5-1-2023 09:00:00"
        },
    "C8":
        {
            "name" : "Varun",
            "ID" : "C8",
            "Dept" : "CSE",
            "year" : 2,
            "last_attendance" : "4-1-2023 09:00:00"
        }

}

for key,value in data.items():
    ref.child(key).set(value)

