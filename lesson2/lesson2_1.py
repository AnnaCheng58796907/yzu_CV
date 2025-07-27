import cv2

img1 = cv2.imread('Building7.jpg', cv2.IMREAD_GRAYSCALE)
print('列印灰階影像的屬性:')
print(f"shape: {img1.shape}")
print(f"size: {img1.size}")
print(f"dtype: {img1.dtype}")

img2 = cv2.imread('Building7.jpg')
print('列印彩色影像的屬性:')
print(f"shape: {img2.shape}")
print(f"size: {img2.size}")
print(f"dtype: {img2.dtype}")
