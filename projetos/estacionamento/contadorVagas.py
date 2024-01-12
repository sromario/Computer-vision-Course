import cv2
import pickle
import numpy as np

#chamar arquivo criado com capturar
with open ("projetos/estacionamento/vagas.pkl", "rb") as arquivo:
    vagas = pickle.load(arquivo)

#chamar video
video = cv2.VideoCapture("projetos/estacionamento/videoEstacionamento.mp4")

#iniciar video e converte ele para: cinza,binary,medianblur. para melhor identificação do espaço
#usar kenel e dil para melhorar identificação
while True:
    check, img = video.read()
    img = cv2.resize(img,(800,500))
    imgCinza = cv2.cvtColor(img, cv2.COLOR_RGBA2GRAY)
    imgTh = cv2.adaptiveThreshold(imgCinza, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,25,16)

    imgMedia = cv2.medianBlur(imgTh,5)
    kernel = np.ones((3,3),np.int8)
    imgDil = cv2.dilate(imgMedia,kernel)
    vagasAbertas = 0

    #definir cordenadas da lista vagas
    #contar o numero de vagas em aberto
    #inserir texto para exibir quantidade de retangulos verdes, que representam vagas livres
    for x,y,w,h in vagas:
        vaga = imgDil[y:y+h,x:x+w]
        cont = cv2.countNonZero(vaga)
        cv2.putText(img,str(cont),(x,y-10),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 0.5, (255,255,255),1)
        if cont <400:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2) #colocar o retangulo verde
            vagasAbertas = vagasAbertas+1
        else:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2) #colocar o retangulo vermelho
        cv2.rectangle(img,(90,0),(415,60),(0,255,255),-1)
        cv2.putText(img,f"LIVRE:{vagasAbertas}/69", (95,45),cv2.FONT_HERSHEY_SIMPLEX, 1.5,(255,255,255),5)
               


    #exibir e encerrar programa caso aperte "esc"
    cv2.imshow("video", img)
    #cv2.imshow("video1", imgDil)
    if cv2.waitKey(10) == 27:
        break