import cv2
import imutils 
import os 
import numpy as np

nombreObjeto = 'Objeto'
if not os.path.exists(nombreObjeto+'/data'):
    print ('Carpeta creada:')
    os.makedirs(nombreObjeto+'/data'+'/p')
    os.makedirs(nombreObjeto+'/data'+'/n')

captura = cv2.VideoCapture(0, cv2.CAP_DSHOW)

x1,y1 = 190, 80
x2,y2 = 450, 398

contador = 0

while True:
    ret, frame = captura.read()
    if ret == False:
        break
    imAux = frame.copy()
    cv2.rectangle(frame, (x1,y1),(x2,y2),(255,0,0),2)
    
    objeto = imAux[y1:y2,x1:x2]
    objeto = imutils.resize(objeto,width=38)

    k = cv2.waitKey(1)
    if k == ord ('f'):
        #se debe seleccionar la ruta adecuada para el almacenamiento de las imagenes positivas/negativas
        cv2.imwrite(nombreObjeto+'/data'+'/p'+'/objeto_{}.jpg'.format(contador),objeto)
        print ('Imagen guardada: '+'/objeto_{}.jpg'.format(contador))
        contador = contador +1

    if k == 27:
        break

    cv2.imshow('frame',frame)
    cv2.imshow('objeto',objeto)
captura.release()
cv2.destroyAllWindows()
