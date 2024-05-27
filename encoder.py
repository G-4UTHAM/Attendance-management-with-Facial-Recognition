import cv2
import face_recognition as fr
import pickle
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://it-project-face-attendance-default-rtdb.firebaseio.com/",
    'storageBucket': "it-project-face-attendance.appspot.com"
})

folderImagePath='images'
ImageList=os.listdir(folderImagePath)
imgList=[]
studentIds=[]
for path in ImageList:
    imgList.append(cv2.imread(os.path.join(folderImagePath,path)))
    studentIds.append(os.path.splitext(path)[0])

    fileName = f'{folderImagePath}/{path}'
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)

print(len(imgList))
print(studentIds)


def encoder(imgList):
    encodeList=[]
    for img in imgList:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode=fr.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

encodeList=encoder(imgList)
print('Encoded')

encodedIds=[encodeList,studentIds]

file = open('EncodeFile.p','wb')
pickle.dump(encodedIds,file)
file.close()
print('Done')