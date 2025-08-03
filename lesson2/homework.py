import cv2
import numpy as np

img = cv2.imread('mountain.jpg')
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv_img)
cv2.namedWindow('mountain', cv2.WINDOW_NORMAL)
cv2.imshow('mountain', img)
ret_value = cv2.waitKey(0)
while ret_value != ord('q'):
    if ret_value == ord('w'):
        if np.all(h > 179):
            h.fill(179)
        else:
            h[:, :] += 5
    elif ret_value == ord('s'):
        if np.all(h < 0):
            h.fill(0)
        else:
            h[:, :] -= 5
    elif ret_value == ord('e'):
        s.fill += 5
        if s.fill > 255:
            s.fill = 255
    elif ret_value == ord('d'):
        s.fill -= 5
        if s.fill < 0:
            s.fill = 0
    elif ret_value == ord('r'):
        v.fill +=5
        if v.fill > 255:
            v.fill = 255
    elif ret_value == ord('f'):
        v.fill -=5
        if v.fill < 0:
            v.fill = 0
    elif ret_value == ord('y'):
        hsv_img = img
        hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        h, s, v = cv2.split(hsv_img)
    hsv_img = cv2.merge([h, s, v])
    cv2.imshow('mountain', hsv_img)
    cv2.waitKey(0)

cv2.destroyAllWindows()
