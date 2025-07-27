import cv2

img = cv2.imread('coca-cola-logo.png')

cv2.imshow("MyPicture", img)
ret_value = cv2.waitKey(5000)  # 0是無限等待，5000是等待5秒
cv2.destroyWindow("MyPicture")
print(f"ret_value: {ret_value}")
