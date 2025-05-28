# Завдання 1
# Відкрийте відео з файлу data\lesson7\meter.mp4.
# Проведіть бінарізацію кадрів та збережіть в новий файл.
# Можливо очистіть від шуму або наведіть різкість через
# bilateralFilter

# bilaterian - не побачив якогось ефекту, тому спробував РОЗМИТТЯ-НАВЕДЕННЯ_РІЗКОСТІ

import cv2
import numpy as np
import utils


# @utils.trackbar_decorator(BFks=(9, 9), BFsigmaX=(1, 10),
#                           alpha= (3, 10),
#                           Blurks=(9, 9), BlursigmaX=(10, 10),
#                           binar_thresh=(75, 178))
def image_maker_BilFiltANDBinar(img, BFks=9, BFsigmaX=1, alpha=3, Blurks=9, BlursigmaX=10, binar_thresh=82):

                                            # binar_thresh=82 (все чітко але невидно першої цифри 20 - 52(щоб побачити цифру 20)

    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = img

    if BFks %2 == 1:
        img_1 = cv2.GaussianBlur(gray,  # оригільне зображення
                                   ksize=(BFks, BFks),  # розмір ядра\фільра\рамки
                                   sigmaX=BFsigmaX  # чим більше тим сильніше розмиття
                                   )
    else:
        BFks += 1
        img_1 = cv2.GaussianBlur(gray,  # оригільне зображення
                                   ksize=(BFks, BFks),  # розмір ядра\фільра\рамки
                                   sigmaX=BFsigmaX  # чим більше тим сильніше розмиття
                                   )

    result = img_1.copy()

    #     # НАВЕДЕННЯ РІЗКОСТІ - використовувати після розмиття
    alp = alpha

    if Blurks %2 == 1:
        blur = cv2.GaussianBlur(gray,  # оригільне зображення
                                ksize=(Blurks, Blurks),  # розмір ядра\фільра\рамки
                                sigmaX=BlursigmaX  # чим більше тим сильніше розмиття
                                )
    else:
        Blurks += 1
        blur = cv2.GaussianBlur(gray,  # оригільне зображення
                                ksize=(Blurks, Blurks),  # розмір ядра\фільра\рамки
                                sigmaX=BlursigmaX  # чим більше тим сильніше розмиття
                                )

    result = (1 + alp) * img_1 - (alp * blur)

    result = np.clip(result, 0, 255)
    result = result.astype(np.uint8)
    #     # НАВЕДЕННЯ РІЗКОСТІ - кінець

    # binarization
    threshold = binar_thresh  # # обираємо поріг
    total = result.copy()
    mask = total > threshold
    total[mask] = 255
    total[~mask] = 0

    return total


cap = cv2.VideoCapture('data\lesson7\meter.mp4')
#
# # тест опрацювання зоображення
# err, frame = cap.read()
# # Gray
# frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#
# # Resize
# frame = cv2.resize(frame, None, fx=0.5, fy=0.5)
#
# # binarization
# threshold = 75 # # обираємо поріг
# binar = frame.copy()
# mask = binar > threshold
# binar[mask] = 255
# binar[~mask] = 0
#
# # # bilaterian - не побачив якогось ефекту, тому спробував РОЗМИТТЯ-НАВЕДЕННЯ_РІЗКОСТІ
# bilat = cv2.bilateralFilter(frame,  # оригільне зображення
#                                      d=5,  # розмір ядра\фільра\рамки
#                                      sigmaColor=72,  # впливає на коефіцієнт за кольором
#                                      sigmaSpace=75,)  # вплива на коефіцієнти як в гауса
#
# result = image_maker_BilFiltANDBinar(frame)
#
# cv2.imshow('Frame', frame)
# cv2.imshow('binar', binar)
# cv2.imshow('bilat', bilat)
# # cv2.imshow('res', result)
# cv2.waitKey(0)

writer = None

while True:
    err, frame = cap.read()

    if not err:
        print('Відсутній кадр відео.')
        break

    # Gray
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Resize
    frame = cv2.resize(frame, None, fx=0.5, fy=0.5)

    result = image_maker_BilFiltANDBinar(frame)

    # НАЛАШТУВАННЯ ЗАПИСУ ВІДЕО
    if writer is None:
        height, width = result.shape
        writer = cv2.VideoWriter('data/lesson7/DZ5.mp4',
                                 cv2.VideoWriter_fourcc(*'mp4v'),
                                 25,
                                 (width, height),
                                 isColor=False)

    writer.write(result)  # Запис кадру у відео

    cv2.imshow('Result', result)
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break
