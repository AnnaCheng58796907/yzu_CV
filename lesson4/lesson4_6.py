import cv2

# 透明度
img = cv2.imread("street.png", cv2.IMREAD_UNCHANGED)
cv2.imshow("Before", img)
print(f"修改前[10, 50] = \n{img[10, 50]}")
print(f"修改前[50, 99] = \n{img[50, 90]}")
print("-"*70)
img[0:200, 0:200, 3] = 128
print(f"修改後[10, 50] = \n{img[10, 50]}")
print(f"修改後[50, 99] = \n{img[50, 90]}")
cv2.imwrite("street128.png", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
