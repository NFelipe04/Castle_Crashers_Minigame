import cv2
from PIL import Image
import numpy as np
from pathlib import Path

yellow = [102, 227, 254]
red = [102, 102, 254]
green = [125, 254, 155]
blue = [254, 165, 102]


def limites(color):

    c = np.uint8([[color]])

    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)

    lowerLimit = hsvC[0][0][0] - 0, 130, 130
    upperLimit = hsvC[0][0][0] + 10, 255, 255

    lowerLimit = np.array(lowerLimit, dtype=np.uint8)
    upperLimit = np.array(upperLimit, dtype=np.uint8)

    return lowerLimit, upperLimit

imagem = cv2.imread("Midias/castle_crashers02.png")

imagem = cv2.resize(imagem, (900, 900))

hsvImage = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)

lowerLimit, upperLimit = limites(color=blue)

# Azul
lowerBlue, upperBlue = limites(blue)
maskBlue = cv2.inRange(hsvImage, lowerBlue, upperBlue)


# Vermelho
lowerRed, upperRed = limites(red)
maskRed = cv2.inRange(hsvImage, lowerRed, upperRed)


# Verde
lowerGreen, upperGreen = limites(green)
maskGreen = cv2.inRange(hsvImage, lowerGreen, upperGreen)


# Amarelo
lowerYellow, upperYellow = limites(yellow)
maskYellow = cv2.inRange(hsvImage, lowerYellow, upperYellow)

mask_all = maskYellow | maskGreen | maskRed | maskBlue

contornos, _ = findContours = cv2.findContours(
                mask_all,
                cv2.RETR_EXTERNAL,
                cv2.CHAIN_APPROX_SIMPLE)



for contorno in contornos:
    
    x, y, w, h = cv2.boundingRect(contorno)

    cv2.rectangle(
        imagem,
        (x, y),
        (x + w, y + h),
        (0, 255, 0), 2)

cv2.imshow("frame", imagem)

while True:

    tecla = cv2.waitKey(1)

    if tecla == 27:
        break

cv2.destroyAllWindows()