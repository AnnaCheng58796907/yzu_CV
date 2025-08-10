import cv2

img = cv2.imread("leclerc_small.png")
cv2.imshow("Before", img)
print(f"修改前[65, 165] = \n{img[65, 165]}")
print(f"修改前[75, 165] = \n{img[75, 165]}")
print(f"修改前[85, 165] = \n{img[85, 165]}")

# 紫色長條
for y in range(60, 70):
    for x in range(130, 200):
        img[y, x] = [255, 0, 255]

# 白色長條
img[70:80, 130:200] = 255

# 黃色長條
img[80:90, 130:200] = [0, 255, 255]

cv2.imshow("After", img)
print(f"修改後[65, 165] = \n{img[65, 165]}")
print(f"修改後[75, 165] = \n{img[75, 165]}")
print(f"修改後[85, 165] = \n{img[85, 165]}")

cv2.waitKey(0)
cv2.destroyAllWindows()
