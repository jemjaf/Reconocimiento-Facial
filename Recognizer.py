import cv2
import os

dataPath = './Data/'
Nombres = os.listdir(dataPath)

faceRecognizer = cv2.face.LBPHFaceRecognizer_create()
faceRecognizer.read('Modelo.xml')

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

#colors BGR
blue, green, red, black = (255, 0, 0), (0,255,0), (0,0,255), (0,0,0)

verificado, tiempo, maxTime, auth, color = 0, 0, 200, "", black

while True:
    ret, frame = cap.read()
    if ret == False: break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    auxFrame = gray.copy()
    faces = faceClassif.detectMultiScale(gray, 1.3, 5)
    
    for (x,y,h,w) in faces:
        face = auxFrame[y:y+h, x:x+w]
        face = cv2.resize(face, (720,720), interpolation=cv2.INTER_CUBIC)
        result = faceRecognizer.predict(face)
        
        if(tiempo<=maxTime):
            if(verificado/maxTime>=0.8):
                auth, color="Reconocido", green
            else:
                auth="No reconocido"

            if result[1]<=20:
                cv2.putText(frame, '{}'.format(result[1]), (x,y-5), 1, 1.3, blue, 1, cv2.LINE_AA)
                cv2.putText(frame, '{}'.format(Nombres[result[0]]), (x,y-25), 2, 1.1, blue, 1, cv2.LINE_AA)
                cv2.rectangle(frame, (x,y), (x+w,y+h), blue, 2)
                verificado+=1
            else:
                cv2.putText(frame, '{}'.format(result[1]), (x,y-5), 1, 1.3, red, 1, cv2.LINE_AA)
                cv2.putText(frame, 'Intruso!', (x,y-20), 2, 0.8, red, 1, cv2.LINE_AA)
                cv2.rectangle(frame, (x,y), (x+w,y+h), red, 2)
        else:
            cv2.putText(frame, '{}'.format(result[1]), (x,y-5), 1, 1.3, color, 1, cv2.LINE_AA)
            cv2.putText(frame, auth, (x,y-25), 2, 1.1, color, 1, cv2.LINE_AA)
            cv2.rectangle(frame, (x,y), (x+w,y+h), color, 2)
        tiempo+=1

    cv2.imshow('Reconociendo', frame)
    k = cv2.waitKey(1)
    if k==27 or tiempo==maxTime+60: break
        
cap.release()
cv2.destroyAllWindows()