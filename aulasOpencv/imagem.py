import cv2

img = cv2.imread('farol.jpg') #para ler a imagem, chamando o caminho
imgCinza = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY) # trasforma imagem da variavel img em outra cor 
print(img.shape) #para ver as dimensões da imagem

cv2.imshow('imagem', img) #para exibir a imagem na tela
cv2.imshow('imagem cinza', imgCinza) #para exibir a imagem de outra cor na tela
cv2.waitKey(0) #para travar o frame na tela