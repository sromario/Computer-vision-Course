import cv2

video = cv2.VideoCapture('runners.mp4') #variavel para armazenar caminho do video

#criar loop para mostrar o frame e exibir o video
while True:
 check, imagem = video.read() #variavel (imagem) para chamar o video e ler
 imagemRedim = cv2.resize(imagem,(600,640)) #reajusta tamanho da imagem
 
 cv2.imshow('video', imagemRedim) #para exibir o video


 if cv2.waitKey(10) == 27: #deletei
    break     


# Liberar recursos.
video.release()
VideoWriter.release()
cv2.destroyAllWindows()