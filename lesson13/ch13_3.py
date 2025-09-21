import cv2
import numpy as np

src = cv2.imread('lena.jpg')
cv2.imshow('src', src)
mask = np.zeros(src.shape[:2], np.uint8)        # 建立遮罩, 大小和src相同
bgdModel = np.zeros((1, 65), np.float64)        # 建立內部用暫時計算陣列
fgdModel = np.zeros((1, 65), np.float64)        # 建立內部用暫時計算陣列
rect = (30, 30, 280, 280)                       # 建立ROI區域
src_rect = src.copy()
cv2.rectangle(src_rect, rect[0:2], rect[2:4], (0, 0, 255), 3)
cv2.imshow('Rectangle', src_rect)
# 呼叫grabCut()進行分割, 迭代 3 次, 回傳mask1
# 其實mask1 = mask, 因為mask也會同步更新
mask1, bgd, fgd = cv2.grabCut(src, mask, rect, bgdModel, fgdModel, 3,
                              cv2.GC_INIT_WITH_RECT)
cv2.imshow('mask1', mask1)
# 將 0, 2設為0 --- 1, 3設為1
mask2 = np.where((mask1 == 0) | (mask1 == 2), 0, 1).astype('uint8')
cv2.imshow('mask2', mask2)
dst = src * mask2[:, :, np.newaxis]             # 計算輸出影像
cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
