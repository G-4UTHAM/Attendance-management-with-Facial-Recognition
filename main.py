import cv2
import cvzone
import numpy as np
import os
import sys
import face_recognition as fr
import pickle
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage
from datetime import datetime
selected_option = sys.argv[1]
print(selected_option)

def read_data(filename):
    data = {}
    with open(filename, 'r') as file:
        for line in file:
            key, value = line.strip().split(": ")
            data[key] = int(value)
    return data

def write_data(filename, data):
    with open(filename, 'w') as file:
        for key, value in data.items():
            file.write(f"{key}: {value}\n")

filename = "data.txt"
data = read_data(filename)

# Check if the key exists in the data
data[selected_option] += 1

# Write the updated data back to the file
write_data(filename, data)


cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://it-project-face-attendance-default-rtdb.firebaseio.com/",
    'storageBucket': "it-project-face-attendance.appspot.com"
})
bucket=storage.bucket()
cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

imgBackground = cv2.imread('Resources/background.png')

folderModePath='Resources/Modes'
modePathList=os.listdir(folderModePath)
imgModeList= []
for path in modePathList:
    imgModeList.append(cv2.imread(os.path.join(folderModePath,path)))

#loading encoded file

file=open('EncodeFile.p','rb')
elwid=pickle.load(file)
eList,iDs=elwid
print(iDs)
imgStudent=[]
modeType=0
counter=0
id = -1

while True:
    success, img = cap.read()
    imgS=cv2.resize(img,(0,0),None,0.25,0.25)
    imgS = cv2.cvtColor(imgS,cv2.COLOR_BGR2RGB)
    
    faceCurFrame=fr.face_locations(imgS)
    encodeCurFrame=fr.face_encodings(imgS,faceCurFrame)
    imgBackground[162:162+480,55:55+640]=img
    imgBackground[44:44+633,808:808+414]=imgModeList[modeType]

    if faceCurFrame:
        for encFace,faceLoc in zip(encodeCurFrame,faceCurFrame):
            matches = fr.compare_faces(eList,encFace)
            faceDis = fr.face_distance(eList,encFace)
            print('matches',matches)
            print('Dist',faceDis)

            matchIndex=np.argmin(faceDis)

            if matches[matchIndex]:
                print('Known Face detected')
                print(iDs[matchIndex])
                id=iDs[matchIndex]

                if counter==0:
                    cvzone.putTextRect(imgBackground,'Loading',(275,400))
                    cv2.imshow('Face Attendance',imgBackground)
                    cv2.waitKey(1)
                    counter=1
                    modeType=1

        if counter!=0:
            if counter==1:
                studentsInfo=db.reference(f'Students/{id}').get()
                print(studentsInfo)
                blob=bucket.get_blob(f'images/{id}.jpg')
                array=np.frombuffer(blob.download_as_string(),np.uint8)
                imgStudent=cv2.imdecode(array,cv2.COLOR_BGRA2BGR)

                datetimeObject=datetime.strptime(studentsInfo['Last_attendance_time'],'%Y-%m-%d %H:%M:%S')
                secondsElapsed=(datetime.now()-datetimeObject).total_seconds()
                print(secondsElapsed)
                if secondsElapsed>30:
                    ref=db.reference(f'Students/{id}')
                    studentsInfo[selected_option]+=1
                    ref.child(selected_option).set(studentsInfo[selected_option])
                    ref.child('Last_attendance_time').set(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                else:
                    modType=3
                    counter=0
                    imgBackground[44:44+633,808:808+414]=imgModeList[modeType]

            if modeType!=3:

                if 10<counter<20:
                    modeType=2
                    imgBackground[44:44+633,808:808+414]=imgModeList[modeType]

                if counter<=10:
                    cv2.putText(imgBackground,str(studentsInfo[selected_option]),(861,125),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1)
                    cv2.putText(imgBackground,str(studentsInfo['Course']),(1006,550),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1)
                    cv2.putText(imgBackground,str(id),(1006,493),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1)
                    cv2.putText(imgBackground,str(studentsInfo['Year']),(1025,625),cv2.FONT_HERSHEY_COMPLEX,0.6,(100,100,100),1)
                    cv2.putText(imgBackground,str(studentsInfo['Starting_year']),(1125,625),cv2.FONT_HERSHEY_COMPLEX,0.6,(100,100,100),1)
                    (w,h),_=cv2.getTextSize(studentsInfo['Name'],cv2.FONT_HERSHEY_COMPLEX,1,1)
                    offset=(414-w)//2
                    cv2.putText(imgBackground,str(studentsInfo['Name']),(808+offset,445),cv2.FONT_HERSHEY_COMPLEX,1,(50,50,50),1)
                    imgBackground[175:175+216,909:909+216]=imgStudent
                


            counter+=1

            if counter>=20:
                counter=0
                modeType=0
                studentsInfo=[]
                imgStudent=[]
                imgBackground[44:44+633,808:808+414]=imgModeList[modeType]
    else:
        modType=0
        counter=0




    cv2.imshow('Face Attendance',imgBackground)
    cv2.waitKey(1)

 
