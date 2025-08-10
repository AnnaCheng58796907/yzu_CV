import numpy as np

image = np.zeros((5, 12), np.uint8)
print(f"修改前 image = \n{image}")
print(f"image[1, 4] = {image[1, 4]}")
print("=======分隔線=======")
image[1, 4] = 255
print(f"修改后 image = \n{image}")
print(f"image[1, 4] = {image[1, 4]}")
