import cv2
import numpy as np

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
        if np.any(h >= 179):
            h.fill(179)
        else:
            h[:, :] += 5
    elif ret_value == ord('s'):
        if np.any(h <= 0):
            h.fill(0)
        else:
            h[:, :] -= 5

    # 飽和度(Saturation),數值0~255
    elif ret_value == ord('e'):
        if np.any(s >= 255):
            s.fill(255)
        else:
            s[:, :] += 5
    elif ret_value == ord('d'):
        if np.any(s <= 0):
            s.fill(0)
        else:
            s[:, :] -= 5

    # 明度(Value),數值0~255
    elif ret_value == ord('r'):
        if np.any(v >= 255):
            v.fill(255)
        else:
            v[:, :] += 5
    elif ret_value == ord('f'):
        if np.any(v <= 0):
            v.fill(0)
        else:
            v[:, :] -= 5

    # 回復原影像
    elif ret_value == ord('y'):
        hsv_img = cv2.cvtColor(copy_img, cv2.COLOR_BGR2HSV)
        h, s, v = cv2.split(hsv_img)
    merge_img = cv2.merge([h, s, v])
    again_img = cv2.cvtColor(merge_img, cv2.COLOR_HSV2BGR)
    cv2.imshow('street', again_img)

cv2.destroyAllWindows()
