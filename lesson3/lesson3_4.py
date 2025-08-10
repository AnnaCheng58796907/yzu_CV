import cv2
import numpy as np

height = 160
width = 280
img = np.zeros((height, width, 3), np.uint8)
img[:50, :, 0] = 255  # Blue
img[50:100, :, 1] = 255  # Green
img[100:150, :, 2] = 255  # Red

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
