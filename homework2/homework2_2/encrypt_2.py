import cv2
import numpy as np

src = cv2.imread("leclerc_small.png")
pt_y = src.shape[0]
pt_x = src.shape[1]
h = pt_y // 2
w = pt_x // 2
key = np.random.randint(0, 256, [h, w, 3], np.uint8)

src_encry = [(0, 0),
             (0, pt_x - w),
             (pt_y - h, 0),
             (pt_y - h, pt_x - w)
             ]

for i, j in src_encry:
    src[i:i+h, j:j+w] = key

cv2.imwrite("key_2.png", key)
cv2.imwrite("encrypted_2.png", src)
