import cv2

lisa = cv2.imread('lisaE2.jpg')
# 以二值化偵測影像中的損壞區域
_, mask = cv2.threshold(lisa, 250, 255, cv2.THRESH_BINARY)
# 對於剛才取得的遮罩做形態學處理 (擴展), 使得遮罩完全覆蓋損壞區域。
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
mask = cv2.dilate(mask, kernel)
# 修復影像
dst = cv2.inpaint(lisa, mask[:, :, -1], 5, cv2.INPAINT_TELEA)
# 輸出執行結果
cv2.imshow('lisa', lisa)
cv2.imshow('mask', mask)
cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
