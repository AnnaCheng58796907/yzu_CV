import cv2
import numpy as np

src = cv2.imread("leclerc_small.png")
key = np.random.randint(0, 256, src.shape, np.uint8)
print(src.shape)
cv2.imshow("Leclerc", src)
cv2.imshow("key", key)

img_encry = cv2.bitwise_xor(src, key)  # 加密
img_decry = cv2.bitwise_xor(key, img_encry)  # 解密
cv2.imshow("Encrytion", img_encry)
cv2.imshow("Decrytion", img_decry)

cv2.waitKey()
cv2.destroyAllWindows()
