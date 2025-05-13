# import numpy as np
# import cv2
#
#
# # масив
# # array = np.array([[1, 2, 3], # перший рядок масиву
# #                   [4, 5, 6] # другий рядок масив
# #                   ])
# #
# # print(array)
# #
# # print(array.dtype)  # тип даних одного елемента
# # print(array.shape)  # розмір (рядочки, стовпчики)
# #
# # # індексація
# # print(array[0, 2])   # елемент рядок 0 та стовпчик 2
# # print(array[0])      # рядок з індексом 0
# # print(array[0:2])    # рядки з 0 по 2
# # print(array[:, 1])   # стовпчик з індексом 1
#
#
# # зображення
# # читання
#
# img = cv2.imread("data/lesson1/cameraman.png", # шлях до файлу
#                  cv2.IMREAD_GRAYSCALE          # зображення чорнобіле
#                  )
#
# # print(img)
# # print(img.dtype)
# # print(img.shape)
#
# # uint8 -- ціле число в діапазоні 0 до 255
#
# # виведення
# # cv2.imshow("test img",  # назва зображення
# #            img)
#
# # індексаці
# segment = img[50:200]  # рядки з 50 по 200
#
# print(segment)
# print(segment.dtype)
# print(segment.shape)
#
# #cv2.imshow('segment', segment)
#
# # збільшити всі пікселі у segment на 20
# segment += 20
#
# cv2.imshow("test img",  # назва зображення
#            img)
#
# # головний цикл
# cv2.waitKey(0)

# умови з масивами
# маска для пікселів які більше 128
# mask = img > 128
#
# print(mask.shape)
# print(mask.dtype)
#
# # дісати пікселі, які відповідають масці
#
# # print(img[mask])
#
# img[mask] = 255  # всі пікселі що відповідають масці
# img[~mask] = 0   # всі пікселі що не відповідають масці
#
# cv2.imshow('', img)
# cv2.waitKey(0)

# __________________________________lab

# Завдання 1
# Відкрийте зображення data/lesson1/Lenna.png
# Виведіть на екран розмір зображення, тип даних пікселів
# зображення та саме зображення.
# import cv2
#
# img = cv2.imread('data/lesson1/Lenna.png', cv2.IMREAD_GRAYSCALE)
#
# # print(img.dtype)
# # print(img.shape)
#
# cv2.imshow(' ', img)

# cv2.waitKey(0)

# Завдання 2
# Відкрийте зображення data/lesson1/Lenna.png
# Виведіть на екран такі частини зображення:
#  Верхній лівий кут 100х50
# segment1 = img[0:100, 0:50]
# cv2.imshow('1', segment1)
#
# #  Нижній правий кут 140x70
# segment2 = img[-140:, -70:]
# cv2.imshow('2', segment2)

#  Верхня половина
# segment2 = img[:128, :]
# cv2.imshow('3', segment2)

#  Нижня половина
# segment4 = img[128:, :]
# cv2.imshow('4', segment4)

#  Ліва половина
# segment5 = img[:, :128]
# cv2.imshow('5', segment5)

#  Прави половина
# segment6 = img[:, 128:]
# cv2.imshow('6', segment6)

#  Центральний квадрат 100х100
# segment7 = img[77:-77, 77:-77]
# cv2.imshow('7', segment7)

# Завдання 3
# Відкрийте зображення data/lesson1/Lenna.png
# Створіть наступні зображення:

#  Чорне окрім центрального квадрата 100х100
# img[:, -77:] = 0
# img[:, :77] = 0
# img[-77:, :] = 0
# img[:77, :] = 0

# cv2.imshow('7', img)
#
#
#
# cv2.waitKey(0)