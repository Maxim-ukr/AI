# Для наступних зображень зображень:
#  data/lesson4/apple.png
#  data/lesson4/apple_noised.png
#  data/lesson4/apple_salt_pepper.png
# використовуючи гаусове розмиття, виявлення країв та
# морфологічні оператори, отримайте краї яблука.

import numpy as np
import utils
import cv2

######data/lesson4/apple.png
# img = cv2.imread("data/lesson4/apple.png", cv2.IMREAD_GRAYSCALE)
#
# img = cv2.GaussianBlur(img, (5,5), 2 )
# can = cv2.Canny(img, 80, 200)
# kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
# dilate = cv2.dilate(can, kernel, iterations=3)
# erode = cv2.erode(dilate, kernel, iterations=2)
# dilate = cv2.dilate(erode, kernel, iterations=2)
#
#
# cv2.imshow("original", img)
# #cv2.imshow("eng", eng)
# # cv2.imshow("Canny apple dilate", dilate)
# cv2.imshow("Canny apple erode", erode)
# cv2.waitKey(0)

######data/lesson4/apple_noised.png

# img2 = cv2.imread("data/lesson4/apple_noised.png", cv2.IMREAD_GRAYSCALE)
#
# img2 = cv2.GaussianBlur(img2, (7,7), 7)
# can = cv2.Canny(img2, 90, 120)
# kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
# dilate = cv2.dilate(can, kernel, iterations=2)
# erode = cv2.erode(dilate, kernel, iterations=1)
# dilate = cv2.dilate(erode, kernel, iterations=1)
#
# cv2.imshow("original", img2)
# cv2.imshow("Canny apple dilate", dilate)
# cv2.imshow("Canny apple erode", erode)
# cv2.waitKey(0)
#

# img3 = cv2.imread("data/lesson4/apple_salt_pepper.png", cv2.IMREAD_GRAYSCALE)
# img3 = cv2.GaussianBlur(img3, (9,9), 10 )
# eng = cv2.Canny(img3, 82, 98)
# kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7,7))
# dilate = cv2.dilate(eng, kernel, iterations=2)
# erode = cv2.erode(dilate, kernel, iterations=1)
#
#
# cv2.imshow("original", img3)
# cv2.imshow("Canny apple dilate", dilate)
# cv2.imshow("Canny apple erode", erode)
# cv2.waitKey(0)
#
#
#
#
# # ___________________
#
# @utils.trackbar_decorator(Dkernel=(3, 21), Eiter=(1, 30), Diter=(1, 30))
# def morf(img, Dkernel,Eiter, Diter):
#     # піксель по сусідству -- в сежах квадрату 3х3
#     kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (Dkernel, Dkernel))
#     eroded = cv2.erode(pic1_gray, kernel, iterations=Eiter)
#
#     # dilate(розширення)
#     # якщо навколо пікселя є хоча б один білий -- то піксель стає білим
#     # dilated = cv2.dilate(img, kernel)
#
#     both = cv2.erode(img, kernel, iterations=Eiter)
#     both = cv2.dilate(both, kernel, iterations=Diter)
#
#     return both
#
# @utils.trackbar_decorator(GBkernel=(3,9), GBsigma=(1,9), alp=(1,9), Bkernel=(3,9), Bsigma=(1,9))
# def rizkist(img, GBkernel, GBsigma, alp, Bkernel, Bsigma):
#     if GBkernel %2 == 1:
#         pic = cv2.GaussianBlur(img,
#                                 (GBkernel, GBkernel),
#                                 sigmaX=GBsigma)
#     else:
#         GBkernel += 1
#         pic = cv2.GaussianBlur(img,
#                                (GBkernel, GBkernel),
#                                sigmaX=GBsigma)
#
#     alpha = alp
#
#     if Bkernel %2 == 1:
#         blur = cv2.GaussianBlur(pic,  # оригільне зображення
#                                    ksize=(Bkernel, Bkernel),  # розмір ядра\фільра\рамки
#                                    sigmaX=Bsigma  # чим більше тим сильніше розмиття
#                                )
#     else:
#         Bkernel += 1
#         blur = cv2.GaussianBlur(pic,  # оригільне зображення
#                                 ksize=(Bkernel, Bkernel),  # розмір ядра\фільра\рамки
#                                 sigmaX=Bsigma  # чим більше тим сильніше розмиття
#                                 )
#
#     pic = (1 + alpha) * pic - (alpha * blur)
#
#     pic = np.clip(pic, 0, 255)
#     pic = pic.astype(np.uint8)
#
#     return pic
#
#
# @utils.trackbar_decorator(Dkernel=(3, 21), Eiter=(1, 30), Diter=(1, 30),
#                           GBkernel=(3,9), GBsigma=(1,9), alp=(1,9), Bkernel=(3,9), Bsigma=(1,9),
#                           CanD=(50,178), CanU=(150,255))
# def both(img, Dkernel,Eiter, Diter, GBkernel, GBsigma, alp, Bkernel, Bsigma, CanD, CanU):
#     # МОРФОЛОГІЯ
#     kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (Dkernel, Dkernel))
#     # eroded = cv2.erode(pic1_gray, kernel, iterations=Eiter)
#
#     # dilate(розширення)
#     # якщо навколо пікселя є хоча б один білий -- то піксель стає білим
#     # dilated = cv2.dilate(img, kernel)
#
#     both = cv2.erode(img, kernel, iterations=Eiter)
#     img = cv2.dilate(both, kernel, iterations=Diter)
#
#     # МОРФОЛОГІЯ -кінець
#
#     if GBkernel %2 == 1:
#         pic = cv2.GaussianBlur(img,
#                                 (GBkernel, GBkernel),
#                                 sigmaX=GBsigma)
#     else:
#         GBkernel += 1
#         pic = cv2.GaussianBlur(img,
#                                (GBkernel, GBkernel),
#                                sigmaX=GBsigma)
#
#     alpha = alp
#
#     if Bkernel %2 == 1:
#         blur = cv2.GaussianBlur(pic,  # оригільне зображення
#                                    ksize=(Bkernel, Bkernel),  # розмір ядра\фільра\рамки
#                                    sigmaX=Bsigma  # чим більше тим сильніше розмиття
#                                )
#     else:
#         Bkernel += 1
#         blur = cv2.GaussianBlur(pic,  # оригільне зображення
#                                 ksize=(Bkernel, Bkernel),  # розмір ядра\фільра\рамки
#                                 sigmaX=Bsigma  # чим більше тим сильніше розмиття
#                                 )
#
#     pic = (1 + alpha) * pic - (alpha * blur)
#
#     pic = np.clip(pic, 0, 255)
#     pic = pic.astype(np.uint8)
#
#     # CANNY
#     pic = cv2.Canny(pic,  # зображення де шукаємо межі
#                       CanD,  # нижня межі інтенсивності межі
#                       CanU   # верхня межі інтенсивності межі
#                       )
#
#
#     return pic
#
# pic1_gray = cv2.imread('data/lesson4/apple_noised.png')
# # pic3 = cv2.imread('data/lesson4/apple_salt_pepper.png')
# # pic1_gray = cv2.imread('data/lesson4/apple.png', cv2.IMREAD_GRAYSCALE)
#
# # morfed = morf(pic1_gray)
#
# # rizkisted = rizkist(pic1_gray)
#
# pic_all = both(pic1_gray)
#
# # img = eroded.copy()
# #
# # # Опрацювання зоображення
# #
# #
# #
# # edged = cv2.Canny(pic1_gray,  # зображення де шукаємо межі
# #                   50,  # нижня межі інтенсивності межі
# #                   150   # верхня межі інтенсивності межі
# #                   )
# # #
# #
# #
#
#
#
#
#
# cv2.imshow("pic1.orig", pic1_gray)
# cv2.imshow("all", pic_all)
# # cv2.imshow("morfed", morfed)
# # cv2.imshow("rizkist", rizkisted)
# # cv2.imshow("edged", edged)
# cv2.waitKey(0)
#
#
# # pic2 = cv2.imread('data/lesson4/apple_noised.png')
# # pic3 = cv2.imread('data/lesson4/apple_salt_pepper.png')
#
