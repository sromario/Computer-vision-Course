import cv2


img = cv2.imread('farol.jpg') #para ler a imagem, chamando o caminho
dim = cv2.selectROI(' selecionar recorte', img, False) #para selecionar área desejada
print(dim) #para ver as dimensões selecionadas no dim

#cordenadas obtidas em inteiros
v1 = int(dim[0])
v2 = int(dim[1])
v3 = int(dim[2])
v4 = int(dim[3])

cv2.imshow('imagem', img) #para exibir a imagem na tela
cv2.imshow('recorte', img[v2:v2+v4, v1:v1+v3]) #chamar recorte das cordenadas 

  
cv2.waitKey(0) #para travar o frame na tela