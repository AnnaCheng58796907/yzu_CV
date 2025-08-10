import cv2
import numpy as np

blue_img = np.zeros((100, 150, 3), np.uint8)
blue_img[:, :, 0] = 255
print(f"blue_img = \n{blue_img}]")
cv2.imshow("blue_img", blue_img)

green_img = np.zeros((100, 150, 3), np.uint8)
green_img[:, :, 1] = 255
print(f"green_img = \n{green_img}")
cv2.imshow("green_img", green_img)

red_img = np.zeros((100, 150, 3), np.uint8)
red_img[:, :, 2] = 255
print(f"red_img = \n{red_img}")
cv2.imshow("red_img", red_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
