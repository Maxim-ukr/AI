import cv2
import ultralytics
import numpy as np
#
# # сегментація
#
# img = cv2.imread("data/lesson_seg/human.jpg")
#
# model = ultralytics.YOLO('yolo11n-seg.pt')
# results = model.predict(img,
#                         classes=[0])
#
# # отримати результат для першого зображення
# result = results[0]
#
# print(result)
# print(result.masks)
#
# # візуалізація
# result.show()
#
# # дістати маску
#
# masks = result.masks.data
#
# # перевести в масив numpy
# masks = masks.numpy()
#
# # змінити тип даних на bool
# masks = masks.astype(bool)
#
# # отримати маску для першого об'єкта
# mask = masks[0]
#
# print(mask)
#
# # візуалізація маски
# mask_img = mask * 255
# mask_img = mask_img.astype(np.uint8)
#
# cv2.imshow('mask', mask_img)
#
# # обрахунок площі об'єкту
# area = mask.sum()  # площа в пікселях
#
# pixel_to_meter = 0.000001
#
# area_meter = area * pixel_to_meter
# print(f"Площа в пікселях {area}")
# print(f"Площа в метрах {area_meter}")
#
# # відсоток зайнятої площі від зображення
# area_percent = mask.mean()  # середнє арифметичне
#
# print(f"Площа у відсотках {area_percent}")
#
# # інше зображення як фон
# background = cv2.imread("data/lesson_seg/castello.png")
#
# # зробити фон та оригінальне зображення такогож розміру що й маска
# height, width = mask.shape
# background = cv2.resize(background, (width, height))
# img = cv2.resize(img, (width, height))
#
# print(img.shape)
# print(background.shape)
#
# # змінити фон
#
# new_img = img.copy()
# new_img[~mask] = 255  # зробити фон білим
#
# # змінити фон на картинку
# background[mask] = img[mask]
#
# cv2.imshow('white background', new_img)
# cv2.imshow('img background', background)
#
#
# cv2.waitKey(0)

# _________________________________________

# Завдання 1
# Відкрийте зображення data/lesson_seg/crop3.jpg
# Проведіть сегментацію зображення використовуючи
# модель data/lesson_seg/crop-seg.pt
# Покажіть усі маски рослин з підписами назви цієї
# рослини.
# Покажіть також самі рослини, для цього застосуйте
# маску, і всі зайві пікселі замініть на 255(зробити білий фон)

img = cv2.imread("data/lesson_seg/crop3.jpg")

model = ultralytics.YOLO('data/lesson_seg/crop-seg.pt')

results = model.predict(img)

result = results[0]

# print(result)
print(result.boxes)

masks = result.masks.data.numpy()


result.show()
for i, mask in enumerate(masks):
    img2 = img.copy()

    img2 = cv2.resize(img2, mask.shape)

    p_name_inx = int(result.boxes.cls[i])
    p_name = result.names[p_name_inx]

    conf = result.boxes.conf[i] * 100

    mask = mask.astype(bool)

    img2[~mask] = 255

    cv2.imshow(f"PLANT {p_name}# {i}, with conf {conf:.2f}", img2)

cv2.waitKey(0)

# Завдання 2
# Відкрийте зображення data/lesson_seg/crop3.jpg
# Проведіть сегментацію зображення
# Порахуйте розмір кожної рослини(площа маски)
# Покажіть найбільшу рослину кожного виду