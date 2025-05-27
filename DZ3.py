# Завдання 1
# Відкрийте зображення data/lesson3/sonet.png. Проведіть
# бінарізацію.
# Обов’язково використайте:
#  розмиття або наведення різкості
#  адаптивну бінарізацію
#  очищеня шумів
# import cv2
# import utils
#
# @utils.trackbar_decorator(GSks=(1,9), GSsigmaX=(1,10),
#                           ATks=(7,9), ATsigma=(4,10),
#                           BFk=(3,9), BFSC=(75,100), BFSS=(75,100))
# def image_maker(img, GSks, GSsigmaX, ATks, ATsigma, BFk, BFSC, BFSS):
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
#     # розмиття
#     if GSks %2 == 1:
#         result = cv2.GaussianBlur(gray,  # оригільне зображення
#                                 ksize=(GSks, GSks),  # розмір ядра\фільра\рамки
#                                 sigmaX=GSsigmaX  # чим більше тим сильніше розмиття
#                                 )
#     else:
#         GSks +=1
#         result = cv2.GaussianBlur(gray,  # оригільне зображення
#                                     ksize=(GSks, GSks),  # розмір ядра\фільра\рамки
#                                     sigmaX=GSsigmaX  # чим більше тим сильніше розмиття
#                                     )
#
#     # # бінарізація(адаптивна)
#     if ATks %2 ==1:
#         result = cv2.adaptiveThreshold(result,  # оригільне зображення(чорнобіле)
#                                         255,  # інтенсивність пікселів білого кольору
#                                         cv2.ADAPTIVE_THRESH_GAUSSIAN_C,  # алгоритм як рахувати threshold
#                                         cv2.THRESH_BINARY,  # тип бінарізації
#                                         ATks,  # розмір ядра\фільра\рамки
#                                         ATsigma,  # наскільки сильною є бінарізацію
#                                         )
#     else:
#         ATks += 1
#         result = cv2.adaptiveThreshold(result,  # оригільне зображення(чорнобіле)
#                                        255,  # інтенсивність пікселів білого кольору
#                                        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,  # алгоритм як рахувати threshold
#                                        cv2.THRESH_BINARY,  # тип бінарізації
#                                        ATks,  # розмір ядра\фільра\рамки
#                                        ATsigma,  # наскільки сильною є бінарізацію
#                                        )
#
#     # Чогось не помітив, що б bilateralFilter працював
#     if BFk %2 ==1:
#         result = cv2.bilateralFilter(result,  # оригільне зображення
#                                         d=BFk,  # розмір ядра\фільра\рамки
#                                         sigmaColor=BFSC,  # впливає на коефіцієнт за кольором
#                                         sigmaSpace=BFSS,  # вплива на коефіцієнти як в гауса
#                                         )
#     else:
#         BFk += 1
#         result = cv2.bilateralFilter(result,  # оригільне зображення
#                                      d=BFk,  # розмір ядра\фільра\рамки
#                                      sigmaColor=BFSC,  # впливає на коефіцієнт за кольором
#                                      sigmaSpace=BFSS,  # вплива на коефіцієнти як в гауса
#                                      )
#
#
#     return result
#
# # @@@@@@@@@@@
# img = cv2.imread('data/lesson3/sonet.png')
# result = image_maker(img)
#
#
# # бінарізація(звичайна)
# # перевести в чорнобілий формат
# # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# #
# # threshold = 150
# #
# # mask = gray > threshold
# #
# # bin[mask] = 255
# # bin[~mask] = 0
#
#
# cv2.imshow('original', img)
# cv2.imshow('Result', result)
# cv2.imshow("simple binarization", bin)
# cv2.waitKey(0)


# Завдання 2
# Відкрийте зображення data/lesson3/sonnet_noised.png.
# Проведіть бінарізацію. Застосуйте код з завдання 1 та
# спробуйте покращити результат
import cv2
import utils


@utils.trackbar_decorator(GSks=(1, 9), GSsigmaX=(1, 10),
                          ATks=(7, 9), ATsigma=(4, 10),
                          BFk=(3, 9), BFSC=(75, 100), BFSS=(75, 100))
def image_maker(img, GSks, GSsigmaX, ATks, ATsigma, BFk, BFSC, BFSS):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # threshold = 75
    # mask = gray > threshold
    # gray[mask] = 255
    # gray[~mask] = 0

    # Чогось не помітив, що б bilateralFilter працював
    if BFk % 2 == 1:
        result = cv2.bilateralFilter(gray,  # оригільне зображення
                                     d=BFk,  # розмір ядра\фільра\рамки
                                     sigmaColor=BFSC,  # впливає на коефіцієнт за кольором
                                     sigmaSpace=BFSS,  # вплива на коефіцієнти як в гауса
                                     )
    else:
        BFk += 1
        result = cv2.bilateralFilter(gray,  # оригільне зображення
                                     d=BFk,  # розмір ядра\фільра\рамки
                                     sigmaColor=BFSC,  # впливає на коефіцієнт за кольором
                                     sigmaSpace=BFSS,  # вплива на коефіцієнти як в гауса
                                     )

    # розмиття
    if GSks % 2 == 1:
        result = cv2.GaussianBlur(result,  # оригільне зображення
                                  ksize=(GSks, GSks),  # розмір ядра\фільра\рамки
                                  sigmaX=GSsigmaX  # чим більше тим сильніше розмиття
                                  )
    else:
        GSks += 1
        result = cv2.GaussianBlur(result,  # оригільне зображення
                                  ksize=(GSks, GSks),  # розмір ядра\фільра\рамки
                                  sigmaX=GSsigmaX  # чим більше тим сильніше розмиття
                                  )

        # # бінарізація(адаптивна)
    if ATks % 2 == 1:
        result = cv2.adaptiveThreshold(result,  # оригільне зображення(чорнобіле)
                                       255,  # інтенсивність пікселів білого кольору
                                       cv2.ADAPTIVE_THRESH_GAUSSIAN_C,  # алгоритм як рахувати threshold
                                       cv2.THRESH_BINARY,  # тип бінарізації
                                       ATks,  # розмір ядра\фільра\рамки
                                       ATsigma,  # наскільки сильною є бінарізацію
                                       )
    else:
        ATks += 1
        result = cv2.adaptiveThreshold(result,  # оригільне зображення(чорнобіле)
                                       255,  # інтенсивність пікселів білого кольору
                                       cv2.ADAPTIVE_THRESH_GAUSSIAN_C,  # алгоритм як рахувати threshold
                                       cv2.THRESH_BINARY,  # тип бінарізації
                                       ATks,  # розмір ядра\фільра\рамки
                                       ATsigma,  # наскільки сильною є бінарізацію
                                       )

    return result


# @@@@@@@@@@@
img = cv2.imread('data/lesson3/sonet_noised.png')
result = image_maker(img)


cv2.imshow('original', img)
cv2.imshow('Result', result)
cv2.waitKey(0)
