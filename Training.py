import cv2, numpy as np, os

dataPath = './Data/'

peopleList = os.listdir(dataPath)

print("Lista de usuarios registrados", peopleList)

labels = []
facesData = []
label = 0

for code in peopleList:
    personPath = dataPath+code
    print("Leyendo Imagenes de :", code)
    
    for fileName in os.listdir(personPath):
        labels.append(label)
        
        facesData.append(
            cv2.imread(personPath+'/'+fileName, 0))
        
    label+=1
    
cv2.destroyAllWindows()

faceRecognizer = cv2.face.LBPHFaceRecognizer_create()
#Entrenamiento
print("Entrenando")
faceRecognizer.train(facesData, np.array(labels))
print("Modelo Entrenado")
#GuardarModelo
faceRecognizer.write('Modelo.xml')
print("Modelo guardado")