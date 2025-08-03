import cv2

img = cv2.imread('street.jpg')
cv2.namedWindow('Original', cv2.WINDOW_NORMAL)
cv2.imshow('Original', img)
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
hue, saturation, value = cv2.split(hsv_img)
hue[:, :] = 50  # equivalent to hue.fill 50
hsv_img1 = cv2.merge([hue, saturation, value])
new_img1 = cv2.cvtColor(hsv_img1, cv2.COLOR_HSV2BGR)
cv2.namedWindow("NEW 1", cv2.WINDOW_NORMAL)
cv2.imshow("NEW 1", new_img1)
hue[:, :] = 150
hsv_img2 = cv2.merge([hue, saturation, value])
new_img2 = cv2.cvtColor(hsv_img2, cv2.COLOR_HSV2BGR)
cv2.namedWindow("NEW 2", cv2.WINDOW_NORMAL)
cv2.imshow("NEW 2", new_img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
