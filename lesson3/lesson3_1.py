import cv2
import numpy as np

fig = np.zeros((50, 200), dtype=np.uint8)
print(fig)
cv2.imshow('fig', fig)

fig1 = np.ones((50, 200), dtype=np.uint8) * 255
print(fig1)
cv2.imshow('fig1', fig1)

cv2.waitKey(0)
cv2.destroyAllWindows()
