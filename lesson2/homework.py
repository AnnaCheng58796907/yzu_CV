import cv2

img = cv2.imread('mountain.jpg')
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv_img)
cv2.namedWindow('mountain', cv2.WINDOW_NORMAL)
cv2.imshow('mountain', img)
ret_value = cv2.waitKey(0)
while ret_value != ord('q'):
    if ret_value == ord('w'):
        h[:, :] += 5
        hsv_img = cv2.merge([h, s, v])
        cv2.imshow('mountain', hsv_img)
        if h.fill == 179:
            h.fill(179)
            hsv_img = cv2.merge([h, s, v])
            cv2.imshow('mountain', hsv_img)
    elif ret_value == ord('s'):
        h.fill -= 5
        if h == 0:
            h.fill = 0
    elif ret_value == ord('e'):
        s += 5

    cv2.waitKey(0)

cv2.destroyWindow('montain')    

'''
def bgr_fill():

    pass


def hsv_fill():
    pass


def a_fill():
    pass


def main():
    ret_value = cv2.waitKey(0)
    if ret_value == ord('h'):
        hsv_fill()
    elif ret_value == ord('a'):
        a_fill()
    elif ret_value == ord('y'):
        bgr_fill(img)
    elif ret_value == ord('q'):
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
'''