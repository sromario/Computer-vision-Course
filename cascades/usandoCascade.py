import cv2

video = cv2.VideoCapture('video.mp4')
classificador = cv2.CascadeClassifier('cascades/haarcascade_fullbody.xml') #posso identificar olhos, face ou corpo chamando o caminho do haarcascade
while True:
    check,img = video.read()
    imgCinza =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    objetos = classificador.detectMultiScale(imgCinza,minSize=(50,50),scaleFactor=1.5) #determinar as cordenadas
    print(objetos)
    for x,y,l,a in objetos:
        cv2.rectangle(img,(x,y),(x+l,y+a),(255,0,0),2) #colocar o retangulo
    
    cv2.imshow('imagem', img)
   
    cv2.waitKey(1)