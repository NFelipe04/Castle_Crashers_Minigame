import cv2

from .blue import lowerBlue, upperBlue
from .green import lowerGreen, upperGreen
from .red import lowerRed1, upperRed1, lowerRed2, upperRed2
from .yellow import lowerYellow, upperYellow


def detectar_cores(imagem):

    hsvImage = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)

    # Azul
    maskBlue = cv2.inRange(
        hsvImage,
        lowerBlue,
        upperBlue
    )

    # Verde
    maskGreen = cv2.inRange(
        hsvImage,
        lowerGreen,
        upperGreen
    )

    # Amarelo
    maskYellow = cv2.inRange(
        hsvImage,
        lowerYellow,
        upperYellow
    )

    # Vermelho
    maskRed1 = cv2.inRange(
        hsvImage,
        lowerRed1,
        upperRed1
    )

    maskRed2 = cv2.inRange(
        hsvImage,
        lowerRed2,
        upperRed2
    )

    maskRed = maskRed1 | maskRed2

    # Junta todas as cores em binariocom o "|"
    mask = maskBlue | maskGreen | maskYellow | maskRed

    # Encontra os contornos
    contornos, _ = cv2.findContours(
        mask,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    return contornos, mask