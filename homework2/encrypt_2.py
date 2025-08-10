import cv2
import numpy as np

src = cv2.imread("leclerc_small.png")
h, w = [x // 2 for x in src.shape[:2]]
key = np.random.randint(0, 256, [h, w], np.uint8)

for y in range(0, 2):
    for x in range(0, 2):
        src[y:y+h, x:x+w] = np.array(key, )
        cv2.imshow("encry", src)
        
#src_encry = cv2.bitwise_xor(src, key)
# cv2.imwrite("key_2.png", key)
# cv2.imwrite("encrypted_2.png", src)

cv2.waitKey()
cv2.destroyAllWindows()
