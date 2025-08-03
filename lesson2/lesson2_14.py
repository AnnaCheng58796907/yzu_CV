import cv2

img = cv2.imread('street.jpg')
cv2.namedWindow('Original', cv2.WINDOW_NORMAL)
cv2.imshow('Original', img)
bgra_img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
b, g, r, a = cv2.split(bgra_img)
a[:, :] = 32  # equivalent to a.fill 50
a32_img = cv2.merge([b, g, r, a])
cv2.namedWindow("a32 img", cv2.WINDOW_NORMAL)
cv2.imshow("a32 img", a32_img)
a.fill(128)
a128_img = cv2.merge([b, g, r, a])
cv2.namedWindow("a128 img", cv2.WINDOW_NORMAL)
cv2.imshow("a128 img", a128_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('a32.png', a32_img)
cv2.imwrite('a128.png', a128_img)
