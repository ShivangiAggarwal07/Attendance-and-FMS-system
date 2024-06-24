import cv2
from deepface import DeepFace
import numpy as np

cap = cv2.VideoCapture(0)


while True:
    ret, frame = cap.read()

    try:
        face_objs = DeepFace.extract_faces(img_path=frame,anti_spoofing = True)
        if face_objs[0]["is_real"]:
                label = "Real Person"
                color = (0, 255, 0) 
        else:
                label = "spoof"
                color = (0, 0, 255)  
        x = face_objs[0]["facial_area"]['x']
        y = face_objs[0]["facial_area"]['y']
        w =face_objs[0]["facial_area"]['w']
        h = face_objs[0]["facial_area"]['h']
        cv2.rectangle(frame, (x,y), (w+x,h+y), color, 2)
        cv2.putText(frame, label, (x,y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)
        

        cv2.imshow('Webcam', frame)
    except Exception as e:
        
        
        cv2.imshow('Webcam', frame)
        print(f"Face not detected: {e}")
    
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()