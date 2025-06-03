import cv2
import runpy as np


def trackbar_decorator(**kwargs):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args):
            window_name = func.__name__
            cv2.namedWindow(window_name)

            trackbar_values = {}

            for param, (min_val, max_val) in kwargs.items():
                cv2.createTrackbar(param, window_name, min_val, max_val, lambda x: None)
                trackbar_values[param] = min_val

            while True:
                for param in kwargs:
                    trackbar_values[param] = cv2.getTrackbarPos(param, window_name)

                result = func(*args, **trackbar_values)
                cv2.imshow(func.__name__, result)

                if cv2.waitKey(1) & 0xFF == 27:
                    break

            cv2.destroyAllWindows()

        return wrapper

    return decorator


