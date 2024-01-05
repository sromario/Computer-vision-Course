import cv2

img = cv2.imread('img02.jpg') #ler a imagem
img = cv2.resize(img,(600,700)) #melhorar dimensões da imagem
imgCinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #mudar imagem para cinza

_,th1 = cv2.threshold(imgCinza,127,255,cv2.THRESH_BINARY) #binarizar a imgCinza #127  é intensidade das letras


th2 = cv2.adaptiveThreshold(imgCinza,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,25,16) #para adaptar a problemas, com aimagem 02(tela estourada)

th3 = cv2.adaptiveThreshold(imgCinza,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,25,16) #para adaptar a problemas(teste outro thresh), com aimagem 02(tela estourada)


cv2.imshow('original', img) #exibir imagem normal
cv2.imshow('binarizada01', th1) #exibir imagem binarizada
cv2.imshow('binarizada02', th2) #exibir imagem binarizada
cv2.imshow('binarizada03', th3) #exibir imagem binarizada
cv2.waitKey(0)