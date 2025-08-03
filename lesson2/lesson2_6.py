import cv2

img = cv2.imread('view.jpg')
print(img[0][0])
print(int(0.299*img[0][0][2] + 0.587*img[0][0][1] + 0.114*img[0][0][0]))
cv2.namedWindow('BGR', cv2.WINDOW_NORMAL)
cv2.imshow('BGR', img)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(img_gray[0][0])
cv2.namedWindow('GRAY', cv2.WINDOW_NORMAL)
cv2.imshow('GRAY', img_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
