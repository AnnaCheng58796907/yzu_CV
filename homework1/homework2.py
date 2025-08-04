import cv2
import numpy as np


def add1_value(two_array: np.ndarray) -> np.ndarray:
    if np.any(two_array >= 179):
        two_array.fill(179)
    else:
        two_array[:, :] += 5
    return two_array


def add2_value(two_array: np.ndarray) -> np.ndarray:
    if np.any(two_array >= 255):
        two_array.fill(255)
    else:
        two_array[:, :] += 5
    return two_array


def reduce_value(two_array: np.ndarray) -> np.ndarray:
    if np.any(two_array <= 0):
        two_array.fill(0)
    else:
        two_array[:, :] -= 5
    return two_array


def disa_image(three_array: np.ndarray) -> np.ndarray:
    three_array = cv2.cvtColor(three_array, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(three_array)
    return h, s, v


def adjust_hsv(img: np.ndarray, ret_value: int) -> np.ndarray:
    copy_img = img.copy()
    h, s, v = disa_image(img)
    # 色相(Hue),數值0~179
    if ret_value == ord('w'):
        add1_value(h)
    elif ret_value == ord('s'):
        reduce_value(h)

    # 飽和度(Saturation),數值0~255
    elif ret_value == ord('e'):
        add2_value(s)
    elif ret_value == ord('d'):
        reduce_value(s)

    # 明度(Value),數值0~255
    elif ret_value == ord('r'):
        add2_value(v)
    elif ret_value == ord('f'):
        reduce_value(v)

    # 回復原影像
    elif ret_value == ord('y'):
        h, s, v = disa_image(copy_img)
    merge_img = cv2.merge([h, s, v])
    again_img = cv2.cvtColor(merge_img, cv2.COLOR_HSV2BGR)
    return again_img


def main() -> None:
    img = cv2.imread('street.jpg')
    cv2.namedWindow('street', cv2.WINDOW_NORMAL)
    cv2.imshow('street', img)
    ret_value = cv2.waitKey(0)
    while ret_value != ord('q'):
        if ret_value == -1:
            ret_value = cv2.waitKey(0)
            continue
        img = adjust_hsv(img, ret_value)
        cv2.imshow('street', img)
        ret_value = cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
