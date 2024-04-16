import cv2

webcam = cv2.VideoCapture(0) #definir variavel para armazenar video e caminho

while True:
 check,img = webcam.read() #ler caminho da camera e armazenar
 
 cv2.imshow('webcamx', img)  #exibir na tela webcam
 
 cv2.waitKey(1)     
