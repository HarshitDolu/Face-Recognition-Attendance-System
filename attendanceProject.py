import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
path='images'
image =[]
classNames=[]
myLis = os.listdir(path)
print(myLis)

for cl in myLis:
    curImg=cv2.imread(f'{path}/{cl}')
    image.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
#print(image)

def findEncodings(image):
    encodeList=[]
    for img in image:
        img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

def markAttendence(name):
    with open('attendance.csv','r+') as f:
        myDataList=f.readlines()
        nameList=[]
        for line in myDataList:
            entry=line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now=datetime.now()
            dtstring=now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dtstring}')

        print(myDataList)


encodeListKnown=findEncodings(image)
print("Encoding complete")

cap=cv2.VideoCapture(0)
while True:
    success, img=cap.read()
    imgS=cv2.resize(img,(0,0),None,0.25,0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    faceLoc = face_recognition.face_locations(imgS)
    #print(" face loc")
    #print(faceLoc)
    encodeCurr = face_recognition.face_encodings(imgS,faceLoc)
    for encodeFace,loc in zip(encodeCurr,faceLoc):
        matches=face_recognition.compare_faces(encodeListKnown,encodeFace)
        faceDis=face_recognition.face_distance(encodeListKnown,encodeFace)
        matchIndex=np.argmin(faceDis)

        if matches[matchIndex]:
            name=classNames[matchIndex].upper()
            print(name)
            markAttendence(name)
            y1,x2,y2,x1=loc
            y1, x2, y2, x1=y1*4,x2*4,y2*4,x1*4
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
            cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)

    cv2.imshow('Webcam',img)
    cv2.waitKey(1)







# step 1
faceLoc =face_recognition.face_locations(imgHar)[0] # 4 values
encodeHar=face_recognition.face_encodings(imgHar)[0]
cv2.rectangle(imgHar,(faceLoc[3],faceLoc[0]),(faceLoc[1],faceLoc[2]),(255,0,255),2)
