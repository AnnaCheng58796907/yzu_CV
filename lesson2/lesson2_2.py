import cv2

pt_y = 169
pt_x = 118
img1 = cv2.imread('Building7.jpg', cv2.IMREAD_GRAYSCALE)
px = img1[pt_y, pt_x]
print('列印灰階影像的數值:')
print(type(px))
print(f"灰階數值: {px}")

img2 = cv2.imread('Building7.jpg')
px2 = img2[pt_y, pt_x]
print('列印彩色影像的數值:')
print(type(px2))
print(f"BGR數值: {px2}")
