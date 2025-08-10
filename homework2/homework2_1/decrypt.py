import cv2

img = cv2.imread("leclerc_small.png")
img_encry = cv2.imread("encrypted.png")
key = cv2.imread("key.png")

img_decry = cv2.bitwise_xor(key, img_encry)  # 解密

if (img == img_decry).all():
    cv2.imwrite("decrypted.png", img_decry)
else:
    cv2.imshow("encrypted", img)
    cv2.imshow("decrypted", img_decry)
    cv2.waitKey()
    cv2.destroyAllWindows()
