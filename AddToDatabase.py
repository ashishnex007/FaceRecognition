import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://face-attendance-92581-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "C0":
        {
            "name": "Rithvik",
            "dept.": "CSE",
            "total_attendance": 6,
            "standing": "G",
            "year": 2,
            "last_attendance": "2023-1-6 09:00:00"
        }
}

for key, value in data.items():
    ref.child(key).set(value)