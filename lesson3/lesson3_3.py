import cv2
import numpy as np

height = 160
width = 280
img = np.zeros((height, width), np.uint8)
# img.fill(255)
for y in range(0, height, 20):
    img[y: y+10, :] = 255
cv2.imshow('ones', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
