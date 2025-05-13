# Завдання 1
# Відкрийте зображення
# data/lesson1/Lenna.png
# Створіть маску для пікселів з
# інтенсивністю більше 128.
# Усі пікселі які відповідають цій масці
# замінити на 255.
# Усі пікселі які не відповідають цій
# масці замінити на 0.
# import cv2
#
# img = cv2.imread("data/lesson1/Lenna.png", cv2.IMREAD_GRAYSCALE)
#
# mask = img > 128
# img[mask] = 255
# img[~mask] = 0
#
# cv2.imshow('Show', img)
#
# cv2.waitKey(0)

# Завдання 2
# Відкрийте зображення data/lesson1/baboo.jpg
# Виведіть таке зображення
# import cv2
#
# img = cv2.imread("data/lesson1/baboo.jpg", cv2.IMREAD_GRAYSCALE)
#
# print(img.shape)
#
# cv2.imshow('Show', img)
#
# segment = img[15:45, 60:-60]
#
# cv2.imshow('Show', segment)
#
# cv2.waitKey(0)
