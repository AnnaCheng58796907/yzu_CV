import cv2

img = cv2.imread("leclerc_small.png", cv2.IMREAD_GRAYSCALE)
cv2.namedWindow("Before image", cv2.WINDOW_NORMAL)
cv2.imshow("Before image", img)
for i in range(70, 80):
    for j in range(130, 200):
        img[i, j] = 255
cv2.namedWindow("After image", cv2.WINDOW_NORMAL)
cv2.imshow("After image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
