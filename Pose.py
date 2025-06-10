# import cv2
# import ultralytics
#
# model = ultralytics.YOLO('yolo11n-pose.pt')
#
# img = cv2.imread('data/lesson_pose/human.jpg')
#
# results = model.predict(img)
#
# res = results[0]
#
# # result_img = res.plot()
# #
# # # вивід результатів
# # print(res)
# # print(res.keypoints)  # ключові точки
# #
# # cv2.imshow("result", result_img)
# # cv2.waitKey(0)
#
# # координати точок
# xy_coords = res.keypoints.xy
#
# # дістати координати точок для першого об'єктів
# xy_coords = xy_coords[0]
#
# # змінити масив на numpy
# xy_coords = xy_coords.numpy()
#
# # змінити тип даних на int
# xy_coords = xy_coords.astype(int)
#
# # координати правої долоні
# x, y = xy_coords[10]
#
# # намалювати круг в даній точці
# # res_img = cv2.circle(
# #     img,  # зображення на якому намалювати коло
# #     (x, y),   # координати центру кола
# #     5,       # радіус у пікселях
# #     (0, 255, 0),  # колір у bgr форматі(тут -- зелений)
# #     -1      # товщина лінії(-1 -- запоанити коло повністю)
# # )
# #
# # cv2.imshow("right arm", res_img)
# # cv2.waitKey(0)
#
#
# # # перевиріти що права долоня вища за праве коліно
# #
# # # коорлинати долоні
# # x_arm, y_arm = xy_coords[10]
# #
# # # коордлинати коліна
# # x_knee, y_knee = xy_coords[14]
# #
# # # вивід коорлинати
# # print(f"Координати долоні -- {x_arm}, {y_arm}")
# # print(f"Координати коліна -- {x_knee}, {y_knee}")
# #
# # # перевірка
# # if y_arm < y_knee:
# #     print("Долоня вище зо коліно")
# # else:
# #     print("Долоня нижче зо коліно")
#
# # перевірити чи правий плече знаходиться правіше за ліву плече
#
# x_right, y_right = xy_coords[6]
# x_left, y_left = xy_coords[5]
#
# # вивід коорлинати
# print(f"Координати лівого плеча  -- {x_left}, {y_left}")
# print(f"Координати правого плеча -- {x_right}, {y_right}")
#
# # перевірка
# if x_right > x_left:
#     text = "human back"  # людина повернута спиною
# else:
#     text = "human face"  # людина повернута до вас
#
# # нанести текст на зображення
#
# img = cv2.putText(
#     img,  # зображення на яке насти текст
#     text,   # сам текст
#     (50, 350),   # координати тексту
#     cv2.FONT_HERSHEY_SIMPLEX,   # шрифт
#     1.5,   # розмір шрифту
#     (255, 255, 255),   # колір у форматі bgr(тут -- білий)
#     2   # товщина лінії
# )
#
# cv2.imshow("", img)
# cv2.waitKey(0)
#


# Завдання 1
# Відкрийте відео data/lesson_pose/sitting.mp4
# Ваша задача рахувати кількість присідань.
# Отримайте перший кадр та виділіть основні точки.
# Отримайте координати однієї з долонь та лівого коліна.
# Вважайте що людина присіла, коли її рука опустилась
# нижче коліна, і піднялась коли її рука опинилась вище коліна.
# Оскільки на відео є декілька людей то обирайте ту, яка
# знаходиться найближче, тобто в якої найбільша площа
# рамки(можете потренуватись на 200-му кадрі)

import cv2
import ultralytics

model = ultralytics.YOLO('yolo11n-pose.pt')

cap = cv2.VideoCapture('data/lesson_pose/sitting.mp4')

squat_count = 0
is_down = False

count = 0

# for i in range(0,200):
#     red, imag = cap.read()
#
# imag = cv2.resize(imag, None, fx=0.1, fy=0.1)
# results = model.predict(imag)
# res1 = results[0]
# cv2.imshow("", res1.plot())
# #print(res1.boxes)
#
#
# xywh = res1.boxes.xywh.numpy()
# w_xywh = xywh[:,2]
# h_xywh = xywh[:,3]
#
# area = w_xywh * h_xywh
#
# index = area.argmax()
#
# res1 = results[0]
# xy = res1.keypoints.xy.numpy()[index]
# xy = xy.astype(int)
# xknee, yknee = xy[14]
#
# res_img = cv2.circle(
#         imag,  # зображення на якому намалювати коло
#         (xknee, yknee),  # координати центру кола
#         5,  # радіус у пікселях
#         (0, 255, 0),  # колір у bgr форматі(тут -- зелений)
#         -1  # товщина лінії(-1 -- запоанити коло повністю)
# )
# cv2.imshow("", res_img)
# print(w_xywh)
# print(h_xywh)
# print(area)

#cv2.waitKey(0)

every_frame = 5
frame_count = 0

while True:
    red, imag = cap.read()
    if not red:
        break

    frame_count += 1
    if frame_count % every_frame != 0:
        continue

    imag = cv2.resize(imag, None, fx=0.1, fy=0.1)
    results = model.predict(imag)
    res1 = results[0]

    xywh = res1.boxes.xywh.numpy()
    w_xywh = xywh[:,2]
    h_xywh = xywh[:,3]

    area = w_xywh * h_xywh

    index = area.argmax()

    points = res1.keypoints
    conf = points.conf.numpy()
    conf = conf[index]
    arm_index = 9 if conf[9] > conf[10] else 10

    # print(conf, arm_index)


    xy = res1.keypoints.xy.numpy()[index]
    xy = xy.astype(int)
    xknee, yknee = xy[14]

    res_img = cv2.circle(
        imag,  # зображення на якому намалювати коло
        (xknee, yknee),  # координати центру кола
        5,  # радіус у пікселях
        (0, 255, 0),  # колір у bgr форматі(тут -- зелений)
        -1  # товщина лінії(-1 -- запоанити коло повністю)
    )

    xarm, yarm = xy[arm_index]

    res_img = cv2.circle(
        imag,  # зображення на якому намалювати коло
        (xarm, yarm),  # координати центру кола
        5,  # радіус у пікселях
        (0, 255, 0),  # колір у bgr форматі(тут -- зелений)
        -1  # товщина лінії(-1 -- запоанити коло повністю)
    )

    if yarm > yknee and not is_down: #рука ниже колена
        squat_count += 1
        is_down = True
    elif yarm < yknee and is_down:
        is_down = False


    res_img = cv2.putText(
        res_img,  # зображення на яке насти текст
        f"count: {squat_count}",   # сам текст
        (50, 50),   # координати тексту
        cv2.FONT_HERSHEY_SIMPLEX,   # шрифт
        1.5,   # розмір шрифту
        (255, 255, 255),   # колір у форматі bgr(тут -- білий)
        2   # товщина лінії
    )



    cv2.imshow("", res_img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


#cv2.waitKey(0)