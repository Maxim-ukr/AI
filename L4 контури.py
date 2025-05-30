import cv2
import numpy as np
import utils


# в opencv кольорове зображення у форматі BGR
# img = cv2.imread("data/lesson4/castello.png")


# межі шукають на чорнобілому зображені
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
# kernel = np.array([[-1, 0, 1],
#                    [-2, 0, 2],
#                    [-1, 0, 1]])
#
# vert = cv2.filter2D(gray, -1, kernel)
#
# kernel = np.array([[-1, -2, -1],
#                    [0, 0, 0],
#                    [1, 2, 1]])
#
# horiz = cv2.filter2D(gray, -1, kernel)
#
# cv2.imshow("original", img)
# cv2.imshow("vertical", vert)
# cv2.imshow("horizontal", horiz)
# cv2.waitKey(0)

# пошук меж

# edged = cv2.Canny(gray,  # зображення де шукаємо межі
#                   100,  # нижня межі інтенсивності межі
#                   150   # верхня межі інтенсивності межі
#                   )
#
# cv2.imshow("original", img)
# cv2.imshow("edged", edged)
# cv2.waitKey(0)

# функція для меж

# @utils.trackbar_decorator(lower=(0, 255), upper=(0, 255))
# def func(img, lower, upper):
#     # перетворення в чорнобіле зображення
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
#     # розмити зображення
#     gray = cv2.GaussianBlur(gray,
#                             (7, 7),
#                             sigmaX=3)
#
#     # алгоритм Canny(пошук меж)
#     edged = cv2.Canny(gray, lower, upper)
#
#     return edged
#
# img = cv2.imread("data/lesson4/apple.png")
#
# func(img)



#
# # ерозія
# # якщо навколо пікселя є хоча б один чорний -- то піксель стає чорним
#
# # піксель по сусідству -- в сежах квадрату 3х3
# kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
# eroded = cv2.erode(img, kernel)
#
# # dilate(розширення?)
# # якщо навколо пікселя є хоча б один білий -- то піксель стає білим
# dilated = cv2.dilate(img, kernel)
#
#
# both = cv2.erode(img, kernel)
# both = cv2.dilate(both, kernel, iterations=2)
#
cv2.imshow("original", img)
# cv2.imshow("eroded", eroded)
# cv2.imshow("dilate", dilated)
# cv2.imshow("both", both)
cv2.waitKey(0)
#
# # _________________________
# # Завдання 1
# # Відкрийте зображення data/lesson4/digit_noised.png.
# # Виконайте наступні дії
# #  Проведіть бінарізацію(можливо з попереднім
# # видаленням шуму)
# #  Застосуйте морфологічні оператори для покращення
# # результату
#
#
# img = cv2.imread("itstep-ai/data/lesson4/digit_noised.png")
#
# g_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
# blur = cv2.GaussianBlur(g_img, (3,3), sigmaX= 0)
#
# kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
#
#
# erode = cv2.erode(blur, kernel, iterations=2)
# mask = erode > 30
#
# erode[mask] = 255
# erode[~mask] = 0
# # adapt_img = cv2.adaptiveThreshold(blur, 255,
# #                                   cv2.ADAPTIVE_THRESH_MEAN_C,
# #                                   cv2.THRESH_BINARY, 7,
# #                                   0.3)
#
#
#
#
# cv2.imshow('res', img)
# cv2.imshow('g_img', g_img)
# cv2.imshow('blur', blur)
# cv2.imshow('erode', erode)
#
#
# #cv2.imshow('adapt_img', adapt_img)
# cv2.waitKey(0)


###2####

# img = cv2.imread("data/lesson4/lego.jpg")
# img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# lower = (45,50,20)
# upper = (75,255,255)
#
# mask_green = cv2.inRange(img_hsv, lower, upper)
#
# cv2.imshow("mask_green", mask_green)
# cv2.waitKey(0)

# img = cv2.GaussianBlur(img, (5,5), 2 )
# eng = cv2.Canny(img, 62, 75)
# kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
# dilate = cv2.dilate(eng, kernel, iterations=3)
# erode = cv2.erode(dilate, kernel, iterations=3)
#
#
#
# #cv2.imshow("original", img)
# cv2.imshow("eng", eng)
# cv2.imshow("dilate", dilate)
# cv2.imshow("erode", erode)
# cv2.waitKey(0)

# @utils.trackbar_decorator(low = (0,255), upper = (0,255))
# def eng_lego(img, low, upper):
#     img = cv2.GaussianBlur(img, (3,3), 4 )
#     eng = cv2.Canny(img, low, upper)
#     return eng
#
# eng_lego(img)

