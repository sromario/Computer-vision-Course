import cv2
import mediapipe as mp

# Dicionário para armazenar usuários e códigos de acesso
usuarios = {}


# Abrir a câmera e entrar no loop de detecção de rosto
webcam = cv2.VideoCapture(0)
solucao_reconhecimento = mp.solutions.face_detection
reconhecer_rostos = solucao_reconhecimento.FaceDetection()
desenho = mp.solutions.drawing_utils



# Função para processar informações do rosto
def processar_rosto(frame, rosto):
    bboxC = rosto.location_data.relative_bounding_box
    ih, iw, _ = frame.shape
    bbox = int(bboxC.xmin * iw), int(bboxC.ymin * ih), \
           int(bboxC.width * iw), int(bboxC.height * ih)

    # Imprimir coordenadas da caixa delimitadora
    print(f"Caixa Delimitadora: {bbox}")

#funcao para cadastrar usuario
def cadastrar_usuario(usuarios):
    nome = input('Qual é o seu nome: ')
    chave = input('Escolha uma chave de acesso de 04 digitos: ')
    usuarios[nome] = chave
    print('Usuário cadastrado com sucesso!')

#funcao para verificar chave de acesso
def verificar_codigo_acesso(usuarios):
    nome = input("Digite o seu nome: ")
    codigo_digitado = input("Digite o código de acesso: ")

    if nome in usuarios and usuarios[nome] == codigo_digitado:
        return True
    else:
        return False
    
#funcao para exibir menu inicial
def exibir_menu():
    print('----------- BEM-VINDO A USFIT ------------')
    print('1 - Entrar')
    print('2 - Cadastrar Usuário')
    opcao = input('Escolha uma opção: ')
    return opcao


# Variável de controle para o loop principal
executar_programa = True

while executar_programa:
    opcao = exibir_menu()

    # entrar
    if opcao == '1':
        if verificar_codigo_acesso(usuarios):

            while True:
                # Ler informações da webcam
                verificador, frame = webcam.read()
                if not verificador:
                    break
                
                # Reconhecer os rostos na imagem
                lista_rostos = reconhecer_rostos.process(frame)

                # Exibir quantidade de rostos detectados
                if lista_rostos.detections:
                    quantidade_rostos = len(lista_rostos.detections)
                    cv2.putText(frame, f"Aluno(a) detectado(a): {quantidade_rostos}", (10, 30),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

                    # Desenhar rosto na imagem
                    for rosto in lista_rostos.detections:
                        desenho.draw_detection(frame, rosto)

                        # Chamar a nova função para processar informações do rosto
                        processar_rosto(frame, rosto)
                else:
                    # Se nenhum rosto for detectado, exibir mensagem de alerta na imagem
                    cv2.putText(frame, "Nenhum rosto detectado!", (10, 30),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

                # chamar webcam e exibir
                cv2.imshow("Rosto na Webcam", frame)

                # encerrar programa com teclas 27 = esc
                if cv2.waitKey(1) == 27:
                    # Defina a variável de controle para False para sair dos loops
                    executar_programa = False
                    break
        else:
            print("Usuário não encontrado.")
            executar_programa = False

    #chama função de cadastro de usuarios, armazenando no dicionario
    elif opcao == '2':
        cadastrar_usuario(usuarios)
    else:
        print('Opção inválida. Escolha "1" ou "2".')

# Liberar recursos e fechar janela da webcam
webcam.release()
cv2.destroyAllWindows()
