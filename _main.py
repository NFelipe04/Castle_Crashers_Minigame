import cv2

from detector_cores._detector_cores import detectar_cores

#imagem temporaria, fazer um sistema que capta a tela em tempo real / formato de video
imagem = cv2.imread("Midias/castle_crashers01.png")

imagem = cv2.resize(imagem, (900, 900))

contornos, mask = detectar_cores(imagem)

for contorno in contornos:

    x, y, w, h = cv2.boundingRect(contorno)

    cv2.rectangle(
        imagem,
        (x, y),
        (x + w, y + h),
        (0, 255, 0),
        2
    )


cv2.imshow("frame", imagem)
cv2.imshow("mask", mask)

while True:

    tecla = cv2.waitKey(1)

    if tecla == 27:
        break

cv2.destroyAllWindows()