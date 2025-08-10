import cv2
import numpy as np

img1 = np.zeros((200, 300, 3), dtype=np.uint8)
img1[:, :, 1] = 255
cv2.imshow("img1", img1)


img2 = np.zeros((200, 300, 3), dtype=np.uint8)
img2[:, :, 2] = 255
cv2.imshow("img2", img2)

m = np.zeros((200, 300, 1), dtype=np.uint8)
m[50:150, 100:200, :] = 255
cv2.imshow("mask", m)

img3 = cv2.add(img1, img2)
cv2.imshow("img1 + img2", img3)

img4 = cv2.add(img1, img2, mask=m)
cv2.imshow("img1 + img2 + mask", img4)

cv2.waitKey(0)
cv2.destroyAllWindows()
