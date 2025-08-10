import cv2
import numpy as np

height = 160
width = 280
img = np.random.randint(256, size=(height, width, 3), dtype=np.uint8)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
