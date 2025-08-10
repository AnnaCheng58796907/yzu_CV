import cv2
import numpy as np


def add_value(two_array: np.ndarray, value: int) -> np.ndarray:
    two_array16 = two_array.astype(np.int16)
    two_array[:] = np.clip(two_array16 + 5, 0, value).astype(np.uint8)
    return two_array


def reduce_value(two_array: np.ndarray, value: int) -> np.ndarray:
    two_array16 = two_array.astype(np.int16)
    two_array[:] = np.clip(two_array16 - 5, 0, value).astype(np.uint8)
    return two_array


def main() -> None:
    img = cv2.imread('street.jpg')
    copy_img = img.copy()
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv_img)
    cv2.namedWindow('street', cv2.WINDOW_NORMAL)
    cv2.imshow('street', img)

    while True:
        ret_value = cv2.waitKey(0)
        if ret_value == ord('q'):
            break

        # 色相(Hue),數值0~179
        elif ret_value == ord('w'):
            add_value(h, 179)
        elif ret_value == ord('s'):
            reduce_value(h, 179)

        # 飽和度(Saturation),數值0~255
        elif ret_value == ord('e'):
            add_value(s, 255)
        elif ret_value == ord('d'):
            reduce_value(s, 255)

        # 明度(Value),數值0~255
        elif ret_value == ord('r'):
            add_value(v, 255)
        elif ret_value == ord('f'):
            reduce_value(v, 255)

        # 回復原影像
        elif ret_value == ord('y'):
            hsv_img = cv2.cvtColor(copy_img, cv2.COLOR_BGR2HSV)
            h, s, v = cv2.split(hsv_img)

        else:
            continue
        merge_img = cv2.merge([h, s, v])
        again_img = cv2.cvtColor(merge_img, cv2.COLOR_HSV2BGR)
        cv2.imshow('street', again_img)

    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
