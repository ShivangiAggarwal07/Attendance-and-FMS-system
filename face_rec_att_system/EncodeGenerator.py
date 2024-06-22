import cv2
import face_recognition
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage
import pickle

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred , {
  'databaseURL' : "https://facerecognitionattsysm-default-rtdb.firebaseio.com/",
  'storageBucket':"facerecognitionattsysm.appspot.com"

})


#importing the list of students
folderPath = 'images'
PathList = os.listdir(folderPath)
print(PathList)
imgList = []
studentsIds = []
for path in PathList:
    imgList.append(cv2.imread(os.path.join(folderPath,path)))

    studentsIds.append(os.path.splitext(path)[0])
    fileName =f'{folderPath}/{path}'
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)
    #print(path)
    #rint(os.path.splitext(path)[0])
print(studentsIds)


def findEncodings(imagesList):
    encodeList = []
    for img in imagesList:

        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode =face_recognition.face_encodings(img)[0]
        encodeList.append(encode)


    return encodeList
print("Encoding Started....")
encodeListKnown = findEncodings(imgList)
encodeListKnownWithIds = [encodeListKnown, studentsIds]

print("Encoding Complete")
file = open("EncoderFile.p",'wb')
pickle.dump(encodeListKnownWithIds,file)
file.close()
print("file saved")