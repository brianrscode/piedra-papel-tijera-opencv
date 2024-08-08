import cv2
import random
import numpy as np
from HandsDetector import HandsDetector


cap = cv2.VideoCapture(2)

img_inicio = cv2.imread("./imgs/4.png")
img_elegir = cv2.imread("./imgs/5.png")
img_ganado = cv2.imread("./imgs/1.png")
img_perdido = cv2.imread("./imgs/2.png")
img_empate = cv2.imread("./imgs/3.png")
img_aux = img_inicio

detector = HandsDetector(max_num_hands=1)

# Combinaciones de dedos
INICIAR_JUEGO = np.array([True, True, False, False, True])
PIEDRA = np.array([False, False, False, False, False])
PAPEL = np.array([True, True, True, True, True])
TIJERA = np.array([False, True, True, False, False])

CASO_GANADOR = ["02", "10", "21"]

THRESHOLD = 10
THRESHOLD_RESTART = 50

count_inicio = 0
count_piedra = 0
count_papel = 0
count_tijera = 0
count_restart = 0

pc_selected_option = False
detect_hand = True

player = None

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = detector.find_hands(frame)

    frame = cv2.hconcat([img_aux, frame])
    landmark_list = detector.find_position_landmarks(frame, draw=False)

    if len(landmark_list) != 0:
        fingers = detector.fingers_up()
        if detect_hand:
            if all(fingers == INICIAR_JUEGO) and pc_selected_option == False:
                if count_inicio >= THRESHOLD:
                    pc = random.randint(0, 2)
                    # print(f"{pc = }")  # Muestra la elección del pc
                    pc_selected_option = True
                    img_aux = img_elegir
                count_inicio += 1

            if pc_selected_option == True:
                if all(fingers == PIEDRA):
                    if count_piedra >= THRESHOLD:
                        player = 0
                    count_piedra += 1
                if all(fingers == PAPEL):
                    if count_papel >= THRESHOLD:
                        player = 1
                    count_papel += 1
                if all(fingers == TIJERA):
                    if count_tijera >= THRESHOLD:
                        player = 2
                    count_tijera += 1

    if player != None:
        detect_hand = False

        if player == pc:
            img_aux = img_empate
        elif str(player) + str(pc) in CASO_GANADOR:
            img_aux = img_ganado
        else:
            img_aux = img_perdido

        count_restart += 1

        if count_restart >= THRESHOLD_RESTART:
            pc_selected_option = False
            detect_hand = True
            player = None
            count_inicio = 0
            count_piedra = 0
            count_papel = 0
            count_tijera = 0
            count_restart = 0
            img_aux = img_inicio


    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'):
        break