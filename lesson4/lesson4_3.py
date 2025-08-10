import numpy as np

# 彩色影像陣列Blue
blue_img = np.zeros((2, 3, 3), np.uint8)
blue_img[:, :, 0] = 255
print(f"Blue = \n{blue_img}")

# 彩色影像陣列Green
green_img = np.zeros((2, 3, 3), np.uint8)
green_img[:, :, 1] = 255
print(f"Green = \n{green_img}")

# 彩色影像陣列Red
red_img = np.zeros((2, 3, 3), np.uint8)
red_img[:, :, 2] = 255
print(f"Red = \n{red_img}")
