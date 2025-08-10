import cv2
import numpy as np

img = cv2.imread("leclerc_small.png")
img_encry = cv2.imread("encrypted_2.png")
key = cv2.imread("key_2.png")

img_key = np.tile(key, (2, 2, 1))

img_decry = cv2.bitwise_xor(img_key, img_encry)
if (img == img_decry).all():
    cv2.imwrite("decrypted_2.png", img_decry)
else:
    cv2.imshow("encrypted", img)
    cv2.imshow("decrypted", img_decry)
    cv2.waitKey()
    cv2.destroyAllWindows()
