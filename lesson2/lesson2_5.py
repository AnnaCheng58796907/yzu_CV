import cv2

img = cv2.imread('view.jpg')
cv2.namedWindow('BGR', cv2.WINDOW_NORMAL)
cv2.namedWindow('RGB', cv2.WINDOW_NORMAL)
cv2.namedWindow('BGR_Again', cv2.WINDOW_NORMAL)
cv2.imshow('BGR', img)

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_bgr = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2BGR)
cv2.imshow('RGB', img_rgb)
cv2.imshow('BGR_Again', img_bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()
