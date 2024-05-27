import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://it-project-face-attendance-default-rtdb.firebaseio.com/"
})

ref=db.reference('Students')

data={
    "70":
    {
        "Name":"Sharath Chandran T",
        "Roll no":"2022BCS0070",
        "Course":"B.Tech CSE",
        "Starting_year":2022,
        "Total_attendance":9,
        "Sex":"M",
        "Year":2,
        "Last_attendance_time":"2023-11-06 01:05:56",
        "IMA211":0,
        "ICS211":0,
        "ICS212":0,
        "ICS213":0,
        "ICS214":0,
        "ICS215":0,
        "ISC211":0,


    },
     "103":
    {
        "Name":"GAUTHAM SURESH",
        "Roll no":"2022BCS0103",
        "Course":"B.Tech CSE",
        "Starting_year":2022,
        "Total_attendance":7,
        "Sex":"M",
        "Year":2,
        "Last_attendance_time":"2023-11-07 02:05:56",
        "IMA211":0,
        "ICS211":0,
        "ICS212":0,
        "ICS213":0,
        "ICS214":0,
        "ICS215":0,
        "ISC211":0

    },
    "34":
    {
        "Name":"Varun Mohan",
        "Roll no":"2022BCS0034",
        "Course":"B.Tech CSE",
        "Starting_year":2022,
        "Total_attendance":12,
        "Sex":"M",
        "Year":2,
        "Last_attendance_time":"2023-11-07 03:25:46",
        "IMA211":0,
        "ICS211":0,
        "ICS212":0,
        "ICS213":0,
        "ICS214":0,
        "ICS215":0,
        "ISC211":0

    },
    "8":
    {
        "Name":"Rohith S",
        "Roll no":"2022BEC0008",
        "Course":"B.Tech ECE",
        "Starting_year":2022,
        "Total_attendance":6,
        "Sex":"M",
        "Year":2,
        "Last_attendance_time":"2023-11-07 03:25:46",
        "IMA211":0,
        "ICS211":0,
        "ICS212":0,
        "ICS213":0,
        "ICS214":0,
        "ICS215":0,
        "ISC211":0

    },
    "46":
    {
        "Name":"Akash Nair",
        "Roll no":"2022BCS0046",
        "Course":"B.Tech CSE",
        "Starting_year":2022,
        "Total_attendance":21,
        "Sex":"M",
        "Year":2,
        "Last_attendance_time":"2023-11-07 12:35:56",
        "IMA211":0,
        "ICS211":0,
        "ICS212":0,
        "ICS213":0,
        "ICS214":2,
        "ICS215":0,
        "ISC211":0

    },
    "37":
    {
        "Name":"Krishnajith",
        "Roll no":"2022BCS0037",
        "Course":"B.Tech CSE",
        "Starting_year":2022,
        "Total_attendance":14,
        "Sex":"M",
        "Year":2,
        "Last_attendance_time":"2023-11-07 04:05:56",
        "IMA211":0,
        "ICS211":0,
        "ICS212":0,
        "ICS213":0,
        "ICS214":0,
        "ICS215":0,
        "ISC211":0

    },
    "7":
    {
        "Name":"Albert Paul Sebastian",
        "Roll no":"2022BCS0007",
        "Course":"B.Tech CSE",
        "Starting_year":2022,
        "Total_attendance":7,
        "Sex":"M",
        "Year":2,
        "Last_attendance_time":"2023-11-07 11:05:56",
        "IMA211":0,
        "ICS211":0,
        "ICS212":0,
        "ICS213":0,
        "ICS214":0,
        "ICS215":0,
        "ISC211":0

    }
    
}

for key,value in data.items():
    ref.child(key).set(value)