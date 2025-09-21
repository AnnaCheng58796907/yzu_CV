import cv2
import numpy as np

# 讀取受損圖像
img = cv2.imread('damaged_photo.jpg')
# 將圖像轉換為灰階色彩
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 創建與圖像大小相同的黑色遮罩
mask = np.zeros(img.shape[:2], dtype=np.uint8)
# 手動設定檢測區域, 矩形區域的座標
x1, y1, x2, y2 = 150, 1, 180, 90
# 取得矩形區域的灰階色彩
roi = gray[y1:y2, x1:x2]
# 在矩形區域內應用 threshold 函數
_, roi_mask = cv2.threshold(roi, 225, 255, cv2.THRESH_BINARY)
# 將處理後的遮罩放回到原遮罩的對應區域
mask[y1:y2, x1:x2] = roi_mask
# 透過形態學操作膨脹, 擴展受損區域, 以確保完全覆蓋
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
mask = cv2.dilate(mask, kernel, iterations=2)
# 使用 inpaint 函數修復圖像
restored_img = cv2.inpaint(img, mask, inpaintRadius=5,
                           flags=cv2.INPAINT_TELEA)
# 顯示原始圖像、遮罩和修復後的圖像
cv2.imshow('Original Image', img)
cv2.imshow('Detected Mask', mask)
cv2.imshow('Restored Image', restored_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
