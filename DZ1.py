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


# ______________________Samostoyatelna
import cv2

img = cv2.imread("data/MyData/Petro0.jpg", cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread("data/MyData/Petro2.jpg", cv2.IMREAD_GRAYSCALE)

# Обчислюємо абсолютну різницю між пікселями
diff = cv2.absdiff(img, img2)

# Встановлюємо чутливість (допустиме відхилення)
threshold = 5

# Створюємо маску, де різниця менша або дорівнює порогу
mask = cv2.inRange(diff, 0, threshold)
#
# img2[diff] = 0
# img[~mask] = 0


cv2.imshow('NoPetro', img)
cv2.imshow('Petro', img2)
cv2.imshow('Petro2', diff)
cv2.imshow('Petro3', mask)

cv2.waitKey(0)
