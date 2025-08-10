import cv2

img = cv2.imread("leclerc_small.png")
img_encry = cv2.imread("encrypted_2.png")
key = cv2.imread("key_2.png")

pt_y = img_encry.shape[0]
pt_x = img_encry.shape[1]
h = pt_y // 2
w = pt_x // 2

src_encry = [(0, 0),
             (0, pt_x - w),
             (pt_y - h, 0),
             (pt_y - h, pt_x - w)
             ]

roi = 
for i, j in src_encry:
    for y, x in src_encry:
        roi[i, j] = 
        src_encry[y:y+h, x:x+w] = cv2.bitwise_xor(key, img_encry[i:i+h, j:j+w])
cv2.imshow(src_encry)
# if (img == img_decry).all():
#     cv2.imwrite("decrypted.png", img_decry)
# else:
#     cv2.imshow("encrypted", img)
#     cv2.imshow("decrypted", img_decry)
#     cv2.waitKey()
#     cv2.destroyAllWindows()
