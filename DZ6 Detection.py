# Завдання 1
# Відкрийте відео з файлу data\lesson8\meetings.mp4
# Застосуйте детекцію та виведіть результат, підберіть
# параметри
# Можете змінити розмір кадру для кращої візуалізації
# Завдання 2
# Почніть показувати відео з моменту, коли людей стало 5

# cv2.resize()
import cv2
import ultralytics
from sympy.codegen import Print

model = ultralytics.YOLO("yolo11s.pt")

# TEST

cap = cv2.VideoCapture('data\lesson8\meetings.mp4')

while True:

    end, frame = cap.read()
    norm_frame = cv2.resize(frame, None, fx=0.2, fy=0.2)

    results = model.track(
        norm_frame,
        conf=0.50,  # мінімальний відсоток з яким можна визначити об'єкт
        iou=0.7,  # якщо для двох рамок iuo менший за це число, то вважаємо що це 2 різних об'єкта
        classes=[0]  # індекси класів(тип об'єктів) які будуть детектитись
        )
    result = results[0]

    boxes = result.boxes
    # print(boxes)

    #

    if len(boxes.id) >= 5:
        result = result.plot()
        print(f"YES! {boxes.id}")
        cv2.imshow('Result', result)



    cv2.imshow('Normal frame', norm_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
