import cv2

#conectar webcam
video = cv2.VideoCapture(0)

#chamar webcam e ler
amostra = 1
while True:
    check, img = video.read()#ler imagem
    imgCinza = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#mudar para cinza

    #caso usuario aperte (S) irá salvar nova img
    if cv2.waitKey(1) & 0xFF == ord('s'): 
        imgR = cv2.resize(imgCinza,(220,220))#redimensionar imagem para tamanho padrão
        cv2.imwrite(f"cascades/fotos/positivas/img {amostra}.jpg", imgR)#salvar
        amostra += 1

    cv2.imshow("captura", img)#ixibir img
    cv2.waitKey(1)


    #obs: faltou treinar pois o cascade trainer gui não pega no linux