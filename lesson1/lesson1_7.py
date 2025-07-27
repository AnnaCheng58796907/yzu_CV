import cv2


cv2.namedWindow("MyPicture")
img = cv2.imread('coca-cola-logo.png')
cv2.imshow("MyPicture", img)
ret = cv2.imwrite('coca-cola-logo-copy.jpg', img)

if ret:
    print("儲存檔案成功!")
else:
    print("儲存檔案失敗!")

cv2.waitKey(0)  # 等待按鍵輸入
cv2.destroyWindow("MyPicture")
cv2.destroyAllWindows()
