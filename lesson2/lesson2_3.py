import cv2

img = cv2.imread('Building7.jpg')
cv2.namedWindow("Building7_1", cv2.WINDOW_NORMAL)
cv2.namedWindow("Building7_2", cv2.WINDOW_NORMAL)
cv2.imshow("Building7_1", img)


pt_y = img.shape[0]
pt_x = img.shape[1]
for y in range(pt_y-50, pt_y):
    for x in range(pt_x-50, pt_x):
        img[y, x] = [255, 255, 255]  # 將指定區域的像素設為白色


cv2.imshow("Building7_2", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
