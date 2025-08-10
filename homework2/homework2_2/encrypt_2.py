import cv2
import numpy as np

src = cv2.imread("leclerc_small.png")
pt_y = src.shape[0]
pt_x = src.shape[1]
h = pt_y // 2
w = pt_x // 2
key = np.random.randint(0, 256, [h, w, 3], np.uint8)

src_key = np.tile(key, (2, 2, 1))

src_encry = cv2.bitwise_xor(src, src_key)

cv2.imwrite("key_2.png", key)
cv2.imwrite("encrypted_2.png", src_encry)
