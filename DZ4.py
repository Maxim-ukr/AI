# Завдання 1
# Для наступних зображень зображень:
#  data/lesson4/apple.png
#  data/lesson4/apple_noised.png
#  data/lesson4/apple_salt_pepper.png
# використовуючи гаусове розмиття, виявлення країв та
# морфологічні оператори, отримайте краї яблука.

import cv2
import numpy as np
import utils

@utils.trackbar_decorator(Dkernel=(3, 21), Eiter=(1, 30), Diter=(1, 30))
def morf(img, Dkernel,Eiter, Diter):
    # піксель по сусідству -- в сежах квадрату 3х3
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (Dkernel, Dkernel))
    eroded = cv2.erode(pic1_gray, kernel, iterations=Eiter)

    # dilate(розширення)
    # якщо навколо пікселя є хоча б один білий -- то піксель стає білим
    # dilated = cv2.dilate(img, kernel)

    both = cv2.erode(img, kernel, iterations=Eiter)
    both = cv2.dilate(both, kernel, iterations=Diter)

    return both

@utils.trackbar_decorator(GBkernel=(3,9), GBsigma=(1,9), alp=(1,9), Bkernel=(3,9), Bsigma=(1,9))
def rizkist(img, GBkernel, GBsigma, alp, Bkernel, Bsigma):
    if GBkernel %2 == 1:
        pic = cv2.GaussianBlur(img,
                                (GBkernel, GBkernel),
                                sigmaX=GBsigma)
    else:
        GBkernel += 1
        pic = cv2.GaussianBlur(img,
                               (GBkernel, GBkernel),
                               sigmaX=GBsigma)

    alpha = alp

    if Bkernel %2 == 1:
        blur = cv2.GaussianBlur(pic,  # оригільне зображення
                                   ksize=(Bkernel, Bkernel),  # розмір ядра\фільра\рамки
                                   sigmaX=Bsigma  # чим більше тим сильніше розмиття
                               )
    else:
        Bkernel += 1
        blur = cv2.GaussianBlur(pic,  # оригільне зображення
                                ksize=(Bkernel, Bkernel),  # розмір ядра\фільра\рамки
                                sigmaX=Bsigma  # чим більше тим сильніше розмиття
                                )

    pic = (1 + alpha) * pic - (alpha * blur)

    pic = np.clip(pic, 0, 255)
    pic = pic.astype(np.uint8)

    return pic

pic1_gray = cv2.imread('data/lesson4/apple.png', cv2.IMREAD_GRAYSCALE)

# morfed = morf(pic1_gray)

rizkisted = rizkist(pic1_gray)

# img = eroded.copy()
#
# # Опрацювання зоображення
#
#
#
# edged = cv2.Canny(pic1_gray,  # зображення де шукаємо межі
#                   50,  # нижня межі інтенсивності межі
#                   150   # верхня межі інтенсивності межі
#                   )
# #
#
#





cv2.imshow("pic1.orig", pic1_gray)
# cv2.imshow("morfed", morfed)
cv2.imshow("rizkist", rizkisted)
# cv2.imshow("edged", edged)
cv2.waitKey(0)


# pic2 = cv2.imread('data/lesson4/apple_noised.png')
# pic3 = cv2.imread('data/lesson4/apple_salt_pepper.png')

