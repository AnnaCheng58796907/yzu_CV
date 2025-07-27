import cv2

img = cv2.imread('coca-cola-logo.png')

cv2.imshow("MyPicture", img)
ret_value = cv2.waitKey(0)  # 0是無限等待，5000是等待5秒
while ret_value != ord("q"):  # 按下q鍵退出
    ret_value = cv2.waitKey(0)  # 等待按鍵輸入
cv2.destroyWindow("MyPicture")
cv2.destroyAllWindows()
