import cv2
import pickle

#chamar o arquivo pgn para tirar as medidas
img = cv2.imread("projetos/estacionamento/estacionamento.png") 

#criar lista vazia para armazenar cordenadas
#percorrer 69 vezes, porque tem 69 vagas
vagas = []
for i in range(69):
    vaga = cv2.selectROI("vagas",img,False) #selecionar o espaço
    cv2.destroyWindow("vagas")
    vagas.append((vaga))

    for x,y,w,h in vagas: #selecionar área com retangulo
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2) 

with open("vagas.pkl", "wb") as arquivo: #após pegar 69 cordenadas, armazenar criandoa arquivo vagas.pkl
    pickle.dump(vagas,arquivo)