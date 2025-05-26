# Відкрийте зображення data/lesson2/darken.png
# Переведіть його в формат HSV
# Далі для каналу value зробіть одну з двох обробок
# 1. Застосуйте вирівнювання гістограм
# 2. Збільшіть значення десь на 20-50%, для цього
# o Помножте усі значення value на відповідне
# число
# o Оскільки ви вийдете за межі діапазону 0-255
# застосуйте
# np.clip(value, 0, 255)
# o Оскільки результат не ціле число
# value.astype(np.unit8)
# o Напишіть для цієї частини функцію з
# utils.trackbar_decorator
# Переведіть результат назад у формат BGR
# Виведіть результат для двох варіантів обробоки
# from distutils.command.install import value

import cv2
import utils
import numpy as np

@utils.trackbar_decorator(alpha=(0,100))
def value_change(img_hsv2, alpha=20):
    value = img_hsv2[:, :, 2]
    value = value * (1 + alpha / 100.0)
    value = np.clip(value, 0, 255)
    img_hsv[:, :, 2] = value.astype(np.uint8)

    result = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2BGR)

    return result


img = cv2.imread("data/lesson2/darken.png")

img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

img_hsv2 = img_hsv.copy()

img_hsv[:,:,2] = cv2.equalizeHist(img_hsv[:,:,2])

# value = img_hsv2[:, :, 0]
# value1 = img_hsv2[:, :, 1]
# value2 = img_hsv2[:, :, 2]

value = value_change(img_hsv2)

cv2.imshow("IMG", img)
cv2.imshow("IMG_hsv eqhist", img_hsv)
cv2.imshow("IMG_hsv v=0", value)
# cv2.imshow("IMG_hsv v=1", value1)
# cv2.imshow("IMG_hsv v=2", value2)
cv2.waitKey(0)

