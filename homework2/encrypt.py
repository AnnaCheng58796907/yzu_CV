import cv2
import numpy as np

src = cv2.imread("leclerc_small.png")
key = np.random.randint(0, 256, src.shape, np.uint8)

img_encry = cv2.bitwise_xor(src, key)  # 加密

cv2.imwrite("key.png", key)
cv2.imwrite("encrypted.png", img_encry)
