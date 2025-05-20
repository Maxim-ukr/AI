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

import cv2

img = cv2.imread("data/lesson2/darken.png")

img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

value = img_hsv[0:180,0:255,:]

print(value)

# img_grsk = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# new_img = cv2.equalizeHist(img_grsk)

# cv2.imshow("eqhist", new_img)
cv2.imshow("IMG_hsv", img_hsv)
cv2.imshow("IMG", img)
cv2.waitKey(0)