import cv2
import numpy as np

# 讀取影像和背景影像
src = cv2.imread('lena.jpg')                # 讀取人物影像
background = cv2.imread('bk1.jpg')          # 讀取背景影像
# 確保背景影像的大小與人物影像相同
background = cv2.resize(background, (src.shape[1], src.shape[0]))
# 建立內部用的 GrabCut 模型
bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)
# 建立 ROI 區域和遮罩
rect = (30, 30, 280, 280)                   # 定義 ROI 區域
mask = np.zeros(src.shape[:2], np.uint8)    # 建立遮罩, 大小與 src 相同
mask[30:324, 30:300] = 3                    # 不確定區域 (GC_PR_BGD)
mask[90:200, 90:200] = 1                    # 確定前景(GC_FGD)
# 執行 GrabCut
mask1, bgd, fgd = cv2.grabCut(
    src, mask, None, bgdModel, fgdModel, 3, cv2.GC_INIT_WITH_MASK)
# 將標記轉換為前景和背景的二值掩膜, # 前景為 1
mask2 = np.where((mask1 == 0) | (mask1 == 2), 0, 1).astype('uint8')
# 提取前景
foreground = src * mask2[:, :, np.newaxis]
# 創建模糊背景, 替換背景
blurred_background = cv2.GaussianBlur(src, (51, 51), 0)  # 模糊背景
final_result = blurred_background * (1 - mask2[:, :, np.newaxis]) + foreground
# 顯示結果
cv2.imshow('src', src)
cv2.imshow('foreground', foreground)
cv2.imshow('blurred_background', blurred_background)
cv2.imshow('final_result', final_result)
cv2.waitKey(0)
cv2.destroyAllWindows()
