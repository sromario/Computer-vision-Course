import cv2

video = cv2.VideoCapture('runners.mp4') #variavel para armazenar caminho do video

while True:
    check,img = video.read() #ler video

    cv2.rectangle(img,(50,50),(200,200),(255,0,0),3) #atribuir retangulo no eixo 50 até 200, cor 255(azul) e largura 3
    cv2.circle(img,(200,200),30,(0,255,0),3)  #atribuir circulo no eixo 200, raio 30 e cor 255(verde) e largura 3
    cv2.line(img,(300,300),(500,300),(0,0,255),3)  #atribuir linha no eixo 300 até 500 e cor 255(vermelho) e largura 3


    texto = 'Piramides formas' #texto para ser inserido
    cv2.putText(img,texto,(200,200),cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,0),3) #inserir texto, chamando imagem e texto, depois definindo cordenada, fonte e tamanho da letra, cor e largura

    cv2.imshow('Formas',img) #exibir imagem com formas
    cv2.waitKey(10)