import sys
import subprocess
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
selected_option = sys.argv[1]

def read_data(filename):
    data = {}
    with open(filename, 'r') as file:
        for line in file:
            key, value = line.strip().split(": ")
            data[key] = int(value)
    return data

filename = "data.txt"
data = read_data(filename)
val=data[selected_option]



cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
   'databaseURL': 'https://it-project-face-attendance-default-rtdb.firebaseio.com/'
})

ref = db.reference('Students')

data = ref.get()
out=["Name","Roll no",selected_option]


key1=list(data.keys())

lout=[]
for k in key1:
    l1=[]
    l1.append(data[k]["Name"])
    l1.append(data[k]["Roll no"])
    l1.append(data[k][selected_option])
    lout.append(l1)
alist={}
for i in lout:
    ch=i[2]
    attpr=ch*100/val
    if attpr<80:
        alist[i[0]]=attpr
print(alist)


def write_data(filename, data):
    with open(filename, 'w') as file:
        for key, value in data.items():
            file.write(f"{key}: {value}\n")

filename = "short.txt"


write_data(filename, alist)

