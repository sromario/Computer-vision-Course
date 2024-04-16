import cv2

img = cv2.imread('objetos.jpg')
img = cv2.resize(img,(600,500))
imgCinza = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgcanny = cv2.Canny(imgCinza,30,200)
imgClose = cv2.morphologyEx(imgcanny,cv2.MORPH_CLOSE,(7,7))

contornos,hierarquia = cv2.findContours(imgClose,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE) #representa os contornos dando "cordenadas" dos contornos

numOB = 1
for cnt in contornos: #para mostrar os contornos nos objetos na imagem
    #cv2.drawContours(img,cnt,-1,(255,0,0),2)
    x,y,w,h = cv2.boundingRect(cnt) #para colocar um retangulo nos objetos, passando cordenadas dos contornos
    recorte = img[y:y+h, x:x+w] #recortando objeto da imagem original
    cv2.imwrite(f'recortes/recorte{numOB}.jpg',recorte) #salvando imagem com nome e numero 
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2) #colocar o retangulo
    numOB += 1



cv2.imshow('original', img)
cv2.imshow('cinza', imgCinza)
cv2.imshow('canny', imgcanny)
cv2.waitKey(0)