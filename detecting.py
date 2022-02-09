import cv2

captura = cv2.VideoCapture(0, cv2.CAP_DSHOW)

cuadradoClassif = cv2.CascadeClassifier('cascade.xml')

while True:
    ret, frame = captura.read()
    gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    objeto = cuadradoClassif.detectMultiScale(gris,scaleFactor=9,minNeighbors=55,minSize=(70,78))

    for (x,y,w,h) in objeto:
        cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
        cv2.putText(frame,'Mario',(x,y-10),2,0.7,(0,255,0),2,cv2.LINE_AA)
    
    cv2.imshow ('frame', frame)
    if cv2.waitKey(1) == 27:
        break

captura.release()
cv2.destroyAllWindows()
