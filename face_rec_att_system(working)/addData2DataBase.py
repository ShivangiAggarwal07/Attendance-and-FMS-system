import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred , {
  'databaseURL' : "https://facerecognitionattsysm-default-rtdb.firebaseio.com/"

})
ref = db.reference('Students')
data = {
    "12313":
        {
            "name": "shubham nandi",
            "medical leave": 2,
            "casual leave":1,
            "total attendance":14,
            "formal leave":1,
            "professional leave":  3,
            "last_attendance_time":"2024-05-11 00:54:34"


        },
    "12314":
        {
            "name": "ashish",
            "medical leave": 3,
            "casual leave":2,
            "total attendance":14,
            "formal leave":1,
            "professional leave":  3,
            "last_attendance_time":"2024-05-11 00:54:34"


        },
    "12315":
        {
            "name": "ratan tata",
            "medical leave": 1,
            "casual leave":3,
            "total attendance":14,
            "formal leave":2,
            "professional leave":  3,


            "last_attendance_time":"2024-05-11 00:54:34"


        },
    "12316":
        {
            "name": "steve job",
            "medical leave": 3,
            "casual leave":0,
            "total attendance":14,
            "formal leave":2,
            "professional leave":  3,
            "last_attendance_time":"2024-05-11 00:54:34"


        },
    "12317":
        {
            "name": "Harsh",
            "medical leave": 3,
            "casual leave":0,
            "total attendance":14,
            "formal leave":2,
            "professional leave":  3,
            "last_attendance_time":"2024-05-11 00:54:34"


        }

}

for key ,value in data.items():
    ref.child(key).set(value)