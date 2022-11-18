import cv2, os, imutils

personCode = 'Jean'
personPath = './Data/' + personCode

if not os.path.exists(personPath):
    os.makedirs(personPath)
    print('Directory created: ', personPath)

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
faceClassif = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
count = 0

while True:
    ret, frame = cap.read()
    if ret == False: break

    frame = imutils.resize(frame, width = 720)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    auxFrame = frame.copy()
    faces = faceClassif.detectMultiScale(gray, 1.3, 5)
    
    for (x,y,h,w) in faces:
        cv2.rectangle(frame, (x,y),(x+w, y+h), (0,255,0), 2)
        rostro = auxFrame[y:y+h, x:x+w]
        rostro = cv2.resize(rostro, (720, 720),
            interpolation=cv2.INTER_CUBIC)
        cv2.imwrite(
            personPath + '/'+personCode+'_{}.jpg'.format(count),
            rostro)
        count+=1
        
    cv2.imshow('Camera', frame)
    if (cv2.waitKey(1) == 27) or count==450: break

cap.release()
cv2.destroyAllWindows()