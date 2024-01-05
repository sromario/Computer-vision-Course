import cv2

img = cv2.imread('piramide.jpg') #ler imagem
img = cv2.resize(img,(200,100)) #diminuir dimensões 
imgCinza = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY) #transforma imagem em cinza
imgBlur = cv2.GaussianBlur(imgCinza,(7,7),0) #para fazer um borrão na imagem
imgcanny = cv2.Canny(img,50,100) #para extrair contornos da imagem
imgdilate = cv2.dilate(imgcanny,(5,5),iterations=5) #para extrair dilatação da imagem
imgerode = cv2.erode(imgcanny,(5,5),iterations=2) #para extrair imagem fragmentada
imgopening = cv2.morphologyEx(imgcanny,cv2.MORPH_OPEN,(5,5))#opening erosão seguida de dilatação // limpa imagem
imgclosing = cv2.morphologyEx(imgcanny,cv2.MORPH_CLOSE,(5,5))#closing contrário de opening (dilatação seguida de erosao)// limpa objeto na imagem



cv2.imshow('img original', img) #exibir imagem
cv2.imshow('img cinza', imgCinza) #exibir imagem cinza
cv2.imshow('img cinza borrado', imgBlur) #exibir imagem desfocada
cv2.imshow('img contorno', imgcanny) #exibir imagem contorno
cv2.imshow('img dilate', imgdilate) #exibir imagem dilatada
cv2.imshow('img dilate', imgerode) #exibir imagem desfragmentada
cv2.imshow('img OPEN', imgopening) #exibir imagem com erosão seguida de erosão
cv2.imshow('img CLOSE', imgclosing) #exibir imagem dilatada seguida de erosão


#tempo de delay e encerrar programa
cv2.waitKey(0) 

  