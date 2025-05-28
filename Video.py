# import numpy as np
# import utils
# import cv2
#
# # # відкрити відео
# # cap = cv2.VideoCapture("data/lesson7/cars.mp4")
# #
# # #cap = cv2.VideoCapture(0)  # відео з вашої камери
# #
# # # отримання кадр
# # ret, img = cap.read()
# #
# # # ret -- True/False чи вдалось отримати кадр
# # print(ret)
# #
# # cv2.imshow('img', img)
# # cv2.waitKey(0)
#
# # показ відое покадрово
#
# cap = cv2.VideoCapture("data/lesson7/cars.mp4")
# cap = cv2.VideoCapture(0)
#
#
# # fps відео
# fps = cap.get(cv2.CAP_PROP_FPS)
#
#
# # збереження відео
# fps = cap.get(cv2.CAP_PROP_FPS)   # чатота відео
# width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)  # ширина кадру
# height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)  # висота кадру
#
# # перевести в тип int
# width = int(width)
# height = int(height)
#
# # кодек
# fourcc = cv2.VideoWriter_fourcc(*'mp4v')
#
# writer = cv2.VideoWriter(
#     "new_video.mp4",  # назва файлу
#     fourcc,   #  кодек
#     fps,      # частота кадрів
#     (width, height),   # розмір кадру
#     isColor=False  # чи кольорове зображення
# )
#
#
# while True:
#     # отримуєте наступний кадр
#     ret, img = cap.read()
#
#     # якщо не вдалось прочитати кадр -- цикл
#     if not ret:
#         break
#
#     # обробка зображення
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
#     edge = cv2.Canny(gray, 50, 100)
#
#     # показ зображення
#     cv2.imshow('video', img)
#     cv2.imshow('gray', gray)
#     cv2.imshow('edge', edge)
#
#     # збереження кадру у файл
#     writer.write(gray)
#
#     # добавити waitKey
#     # cv2.waitKey(1)  # чекати 1 мілісекунду
#     # cv2.waitKey(int(1000 // fps))  # оригільна затримка
#
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
#
# # звільнення пам'яті
# writer.release()
# cap.release()
#
# # закрити усі вікна
# cv2.destroyAllWindows()

# ________________________________________lab

# Завдання 1
# Виведіть відео з файлу data\lesson7\text.mp4 на екран та
# збережіть в новий файл.
# Змініть розмір зображення.
# import cv2
#
#
# cap = cv2.VideoCapture(r'data\lesson7\text.mp4')
# # ret, img = cap.read()
# # if not ret:
# #     print("Не вдалося відкрити відео.")
# #
# # cv2.imshow("frame", img)
# # cv2.waitKey(5000)
#
# width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))# Встановлення FPS
# print(width, height)
# writer = cv2.VideoWriter('data/lesson7/output.mp4',
#                           cv2.VideoWriter_fourcc(*'mp4v'),
#                           30,  # FPS
#                           (width, height)  # Розмір кадру
#                           )
# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break
#
#     # # Зміна розміру кадру
#     resized_frame = cv2.resize(frame, None, fx=0.3, fy=0.3)
#
#     # Відображення кадру
#     cv2.imshow("Resized Frame", resized_frame)
#
#     writer.write(resized_frame)  # Запис кадру у відео
#
#     # Вихід з циклу при натисканні клавіші 'q'
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# writer.release()
# Завдання 2
# Відкрийте відео з файлу data\lesson7\text.mp4. Проведіть
# бінарізацію кадрів та збережіть в новий файл.
# import cv2
# import numpy as np
#
#
# cap = cv2.VideoCapture(r'data\lesson7\text.mp4')
# ret, img = cap.read()
# if not ret:
#     print("Не вдалося відкрити відео.")
#
# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
# img = cv2.GaussianBlur(img,  # оригільне зображення
#                            ksize=(5, 5), # розмір ядра\фільра\рамки
#                            sigmaX=10  # чим більше тим сильніше розмиття
#                            )
#
# binar = cv2.adaptiveThreshold(img,  # оригільне зображення(чорнобіле)
#                                 255, # інтенсивність пікселів білого кольору
#                                 cv2.ADAPTIVE_THRESH_GAUSSIAN_C,  # алгоритм як рахувати threshold
#                                 cv2.THRESH_BINARY,  # тип бінарізації
#                                 11,  # розмір ядра\фільра\рамки
#                                 2,  # наскільки сильною є бінарізацію
#                                 )
#
# cv2.imshow("frame", img)
# cv2.imshow("bin", binar)
#
# cv2.waitKey(0)

# width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))# Встановлення FPS
# print(width, height)
# writer = cv2.VideoWriter('data/lesson7/binar.mp4',
#                           cv2.VideoWriter_fourcc(*'mp4v'),
#                           30,  # FPS
#                           (width, height),  # Розмір кадру
#                           isColor=False
#                           )
# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break
#
#     # # Зміна розміру кадру
#     # resized_frame = cv2.resize(frame, None, fx=0.3, fy=0.3)
#
#     img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#
#     img = cv2.GaussianBlur(img,  # оригільне зображення
#                            ksize=(7, 7),  # розмір ядра\фільра\рамки
#                            sigmaX=10  # чим більше тим сильніше розмиття
#                            )
#     # НАВЕДЕННЯ РІЗКОСТІ - використовувати після розмиття
#     alpha = 2.0
#
#     blur = cv2.GaussianBlur(img,  # оригільне зображення
#                            ksize=(3, 3),  # розмір ядра\фільра\рамки
#                            sigmaX=0  # чим більше тим сильніше розмиття
#                            )
#
#     img = (1 + alpha) * img - (alpha * blur)
#
#     img = np.clip(img, 0, 255)
#     img = img.astype(np.uint8)
#     # НАВЕДЕННЯ РІЗКОСТІ - кінець
#
#     cv2.imshow('Sharp', img)
#
#     binar = cv2.adaptiveThreshold(img,  # оригільне зображення(чорнобіле)
#                                   255,  # інтенсивність пікселів білого кольору
#                                   cv2.ADAPTIVE_THRESH_GAUSSIAN_C,  # алгоритм як рахувати threshold
#                                   cv2.THRESH_BINARY,  # тип бінарізації
#                                   11,  # розмір ядра\фільра\рамки
#                                   2,  # наскільки сильною є бінарізацію
#                                   )
#
#     # Відображення кадру
#     cv2.imshow("Resized Frame", frame)
#     cv2.imshow("Binar", binar)
#
#     writer.write(binar)  # Запис кадру у відео
#
#     # Вихід з циклу при натисканні клавіші 'q'
#     if cv2.waitKey(100) & 0xFF == ord('q'):
#         break
#
# writer.release()

# Завдання 3
# Відкрийте відео з файлу data\lesson7shapes.mp4.
# Проведіть виділення країв на кадрах та збережіть в новий
# файл.
import ultralytics
import torch
import langchain

model = ultralytics.YOLO("yolov8n.pt")
