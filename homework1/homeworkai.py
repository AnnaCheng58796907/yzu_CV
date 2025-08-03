import cv2
import numpy as np

# 讀取影像
img = cv2.imread('mountain.jpg')
if img is None:
    print("錯誤: 無法讀取影像檔。請確認檔案路徑是否正確。")
    exit()

# 備份原始影像，用於重設功能
original_img = img.copy()

# 將影像從 BGR 色彩空間轉換為 HSV
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# 分割 HSV 通道
h, s, v = cv2.split(hsv_img)

# 創建顯示視窗
cv2.namedWindow('mountain', cv2.WINDOW_NORMAL)
cv2.imshow('mountain', img)

print("請在 'mountain' 視窗上使用鍵盤按鍵:")
print("w: Hue +5, s: Hue -5")
print("e: Saturation +5, d: Saturation -5")
print("r: Value +5, f: Value -5")
print("y: 重設影像, q: 關閉視窗")

# 持續等待按鍵
while True:
    ret_value = cv2.waitKey(0) & 0xFF

    if ret_value == ord('q'):
        break
    elif ret_value == ord('w'):
        # 增加 Hue 數值，使用 np.clip 確保數值在 [0, 179] 範圍內
        h = np.clip(h + 5, 0, 179).astype(np.uint8)
    elif ret_value == ord('s'):
        # 減少 Hue 數值
        h = np.clip(h - 5, 0, 179).astype(np.uint8)
    elif ret_value == ord('e'):
        # 增加 Saturation 數值
        s = np.clip(s + 5, 0, 255).astype(np.uint8)
    elif ret_value == ord('d'):
        # 減少 Saturation 數值
        s = np.clip(s - 5, 0, 255).astype(np.uint8)
    elif ret_value == ord('r'):
        # 增加 Value 數值
        v = np.clip(v + 5, 0, 255).astype(np.uint8)
    elif ret_value == ord('f'):
        # 減少 Value 數值
        v = np.clip(v - 5, 0, 255).astype(np.uint8)
    elif ret_value == ord('y'):
        # 重設為原始影像的 HSV 通道
        hsv_img = cv2.cvtColor(original_img, cv2.COLOR_BGR2HSV)
        h, s, v = cv2.split(hsv_img)

    # 合併修改後的 HSV 通道
    merged_hsv = cv2.merge([h, s, v])
    # 將 HSV 影像轉換回 BGR 格式
    adjusted_img = cv2.cvtColor(merged_hsv, cv2.COLOR_HSV2BGR)
    # 顯示調整後的影像
    cv2.imshow('mountain', adjusted_img)

# 關閉所有視窗
cv2.destroyAllWindows()
