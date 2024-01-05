import cv2

img = cv2.imread('farol.jpg') #para ler a imagem, chamando o caminho
dim = cv2.selectROI('selecionar recorte', img, False) #para selecionar área desejada
print(dim) #para ver as dimensões selecionadas no dim
cv2.destroyWindow('selecionar recorte')

#cordenadas obtidas em inteiros
v1 = int(dim[0])
v2 = int(dim[1])
v3 = int(dim[2])
v4 = int(dim[3])

#cv2.imshow('imagem', img) #para exibir a imagem na tela

caminho = 'recortesImagem/' #o caminho da pasta que a imagem vai parar
nome_arquivo = input('digite o nome do arquivo: ') #o arquivo, e e nome

recorte = img[v2:v2+v4, v1:v1+v3]
cv2.imwrite(f'{caminho}{nome_arquivo}.jpg', recorte) #salvando arquivo da pasta
print('imagem salva com sucesso')

#cv2.imshow('recorte', img[v2:v2+v4, v1:v1+v3]) #chamar recorte das cordenadas 

  
cv2.waitKey(0) #para travar o frame na tela