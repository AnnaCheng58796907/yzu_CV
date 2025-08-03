import cv2

img = cv2.imread('street.jpg')
cv2.namedWindow('Original', cv2.WINDOW_NORMAL)
cv2.imshow('Original', img)
blue, green, red = cv2.split(img)
bgr_img = cv2.merge([blue, green, red])
cv2.namedWindow('B->G->R', cv2.WINDOW_NORMAL)
cv2.imshow('B->G->R', bgr_img)

rgb_img = cv2.merge([red, green, blue])
cv2.namedWindow('R->G->B', cv2.WINDOW_NORMAL)
cv2.imshow('R->G->B', rgb_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
