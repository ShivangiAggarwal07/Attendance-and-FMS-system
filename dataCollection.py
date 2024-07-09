from cvzone.FaceDetectionModule import FaceDetector
import cv2
import cvzone
from time import time

##############################################
classID = 0 # 0 is fake, 1 is real
outputFolderPath = 'Dataset/DataCollect'
offsetPercentageW = 10
offsetPercentageH = 20
confidence = 0.8
save = True
blurThreshold = 35 # Larger is more focused

debug = False
camWidth, camHeight = 640, 480
floatingPoint = 6
##############################################

cap = cv2.VideoCapture(0)
cap.set(3, camWidth)
cap.set(4, camHeight)

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

detector = FaceDetector(minDetectionCon=0.5, modelSelection=0)

while True:
    success, img = cap.read()
    imgOut = img.copy()
    img, bboxs = detector.findFaces(img, draw=False)

    listBlur = [] # true or false to check whether face blur or not
    listInfo = [] # the normalized values and the class name for label text file

    if bboxs:
        # for bbox in bboxs:
        #     center = bbox["center"]
        #     x, y, w, h = bbox['bbox']
        #     score = int(bbox['score'][0] * 100)
        #
        #     cvzone.putTextRect(img, f'{score}%', (x, y - 10))
        #     cvzone.cornerRect(img, (x, y, w, h))
        for bbox in bboxs:
            x,y,w,h = bbox["bbox"]
            score = bbox["score"][0]
            print(x,y,w,h)

            # check the score and if good score then allow detection
            if score > confidence:

                # adjusting offset for width of box
                offsetW = (offsetPercentageW / 100)*w
                x = int(x - offsetW)
                w = int(w + offsetW * 2)

                # adjusting offset for height of box
                offsetH = (offsetPercentageH / 100) * h
                y = int(y - offsetH*3)
                h = int(h + offsetH * 3.5)

                # to avoid values below zero i.e when face goes out of frame
                if (x < 0): x = 0
                if (y < 0): y = 0
                if (w < 0): w = 0
                if (h < 0): h = 0

                # find blurriness
                imgFace = img[y:y+h, x:x+w]
                cv2.imshow("Face", imgFace)
                blurValue = int(cv2.Laplacian(imgFace, cv2.CV_64F).var())
                if blurValue>blurThreshold:
                    listBlur.append(True)
                else:
                    listBlur.append(False)

                # normalize values
                ih, iw, _ = img.shape
                xc, yc = x+w/2, y+h/2

                xcn, ycn = round(xc/iw, floatingPoint), round(yc/ih, floatingPoint)
                wn, hn = round(w/iw, floatingPoint), round(h/ih, floatingPoint)
                print(xcn, ycn, wn, hn)

                # to avoid values above 1
                if (xcn > 1): x = 1
                if (ycn > 1): y = 1
                if (wn > 1): w = 1
                if (hn > 1): h = 1

                listInfo.append(f"{classID} {xcn} {ycn} {wn} {hn}\n")

                # Drawing
                cv2.rectangle(imgOut, (x,y,w,h), (255, 0, 0), 3)
                cvzone.putTextRect(imgOut, f'Score: {int(score*100)}% Blur: {blurValue}', (x, y - 20), scale=2, thickness=3)

                if debug:
                    cv2.rectangle(img, (x, y, w, h), (255, 0, 0), 3)
                    cvzone.putTextRect(img, f'Score: {int(score * 100)}% Blur: {blurValue}', (x, y - 20), scale=2,
                                       thickness=3)

        # To save
        if save:
           if all(listBlur) and listBlur!=[]:
                timeNow = time()
                timeNow = str(timeNow).split('.')
                timeNow = timeNow[0] + timeNow[1]
                cv2.imwrite(f"{outputFolderPath}/{timeNow}.jpg", img)
                # Save Label Text File
                for info in listInfo:
                    f = open(f"{outputFolderPath}/{timeNow}.txt", 'a')
                    f.write(info)
                    f.close()




    cv2.imshow("Image", imgOut)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()