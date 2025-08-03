import cv2

img = cv2.imread('mountain.jpg')
cv2.namedWindow('BGR', cv2.WINDOW_NORMAL)
cv2.imshow('BGR', img)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.namedWindow('HSV', cv2.WINDOW_NORMAL)
cv2.imshow("HSV", img_hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()
