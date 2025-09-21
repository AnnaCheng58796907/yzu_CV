import cv2
import numpy as np

src = cv2.imread('hung.jpg')
cv2.imshow('src', src)
mask = np.zeros(src.shape[:2], np.uint8)        # 建立遮罩, 大小和src相同
bgdModel = np.zeros((1, 65), np.float64)        # 建立內部用暫時計算陣列
fgdModel = np.zeros((1, 65), np.float64)        # 建立內部用暫時計算陣列
rect = (10, 30, 380, 360)                       # 建立ROI區域
# 呼叫grabCut()進行分割
cv2.grabCut(src, mask, rect, bgdModel, fgdModel, 3, cv2.GC_INIT_WITH_RECT)
newmask = cv2.imread('hung_mask.jpg', cv2.IMREAD_GRAYSCALE)  # 灰階讀取
cv2.imshow('newmask', newmask)
mask[newmask == 0] = 0                          # 黑色內容則確定是背景
mask[newmask == 255] = 1                        # 白色內容則確定是前景
cv2.grabCut(src, mask, None, bgdModel, fgdModel, 3, cv2.GC_INIT_WITH_MASK)
# 將 0, 2設為0 --- 1, 3設為1
mask = np.where((mask == 0) | (mask == 2), 0, 1).astype('uint8')
dst = src * mask[:, :, np.newaxis]              # 計算輸出影像
cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
