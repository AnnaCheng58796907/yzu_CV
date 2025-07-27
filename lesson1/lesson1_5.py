import cv2

# 設定可調視窗
cv2.namedWindow("MyPicture1")
cv2.namedWindow("MyPicture2", cv2.WINDOW_NORMAL)

img1 = cv2.imread('coca-cola-logo.png')
img2 = cv2.imread('coca-cola-logo.png', cv2.IMREAD_GRAYSCALE)

cv2.imshow("MyPicture1", img1)
cv2.imshow("MyPicture2", img2)

ret_value = cv2.waitKey(0)  # 0是無限等待，5000是等待5秒

cv2.destroyAllWindows()
