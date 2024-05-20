import cv2
import mediapipe as mp

video = cv2.VideoCapture(0)

# Inicializa o módulo de detecção de mãos do MediaPipe
hand = mp.solutions.hands
Hand = hand.Hands(max_num_hands=1)
mpDraw = mp.solutions.drawing_utils


while True:
    # ler e converter video
    check,img = video.read()
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

    # Processa o quadro de vídeo em busca de mãos
    results = Hand.process(imgRGB)
    handspoints = results.multi_hand_landmarks
    
    h,w,_ =img.shape # dimensões da imagem (altura x largura)
    pontos = []
    # Verifica se foram encontradas mãos e desenha os pontos e conexões das mãos detectadas
    if handspoints:
        for points in handspoints:
            print(handspoints)
            mpDraw.draw_landmarks(img,points,hand.HAND_CONNECTIONS)

            # enumerar os pontos da hand // #landmarks: pontos de referencias 
            for id, corte in enumerate(points.landmark): 
                   cx,cy =int(corte.x*w), int(corte.y*h) # extraindo cordenadas
                   cv2.putText(img,str(id),(cx,cy+10),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,0,0),2) #exibir cordenadas na tela com os pontos
                   pontos.append((cx,cy))
                   

        # pontos das pontas dos dedos
        dedos =[8,12,16,20]
        contador = 0

        # ver se a cordenada x está nos dedos e se está baixo ou não
        if points:
            if pontos[4][0] < pontos[2][0]:
                contador += 1
            for x in dedos:
             if pontos[x][1] < pontos[x-2][1]:
                 contador += 1
    
    
        print(contador)

        cv2.putText(img,str(contador),(100,100),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,4,(0,255,0),5)    
    cv2.imshow('imagem', img)  #exibir e encerrar programa
    cv2.waitKey(1)
    
        