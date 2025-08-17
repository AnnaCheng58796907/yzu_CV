import cv2
import numpy as np


def bgr_cmyk(img) -> np.ndarray:
    bgr_norm = img.astype(float) / 255.0

    # 計算 K 通道
    K = 1 - np.max(bgr_norm, axis=2)

    # 防止除以0,設定一個最小閾值
    denominator = 1 - K
    denominator[denominator == 0] = 1e-10

    # 計算 C、M、Y 通道
    C = (1 - bgr_norm[..., 2] - K) / denominator
    M = (1 - bgr_norm[..., 1] - K) / denominator
    Y = (1 - bgr_norm[..., 0] - K) / denominator

    return C, M, Y, K


def cmyk_to_bgr(C, M, Y, K):
    # 確保C, M, Y, K是float，且在0~1範圍內
    B = (1 - Y) * (1 - K) * 255
    G = (1 - M) * (1 - K) * 255
    R = (1 - C) * (1 - K) * 255
    bgr = np.stack([B, G, R], axis=-1).astype(np.uint8)
    return bgr


width = 900
height = int((width / 3) * 2)

# 紅地：CMYK (0%, 100%, 100%, 10%)
red_src = np.ones((height, width, 3), np.uint8) * 255
red_C, red_M, red_Y, red_K = bgr_cmyk(red_src)
red_C = np.zeros_like(red_C) * 0.0
red_M = np.ones_like(red_M) * 1.0
red_Y = np.ones_like(red_Y) * 1.0
red_K = np.ones_like(red_K) * 0.1
red_bgr = cmyk_to_bgr(red_C, red_M, red_Y, red_K)

# 青天：CMYK (100%, 80%, 0%, 20%)
h = red_src.shape[0] // 2
w = red_src.shape[1] // 2
bg_src = np.ones((h, w, 3), np.uint8) * 255
bg_C, bg_M, bg_Y, bg_K = bgr_cmyk(bg_src)
bg_C = np.ones_like(bg_C) * 1.0
bg_M = np.ones_like(bg_M) * 0.8
bg_Y = np.zeros_like(bg_Y) * 0.0
bg_K = np.ones_like(bg_K) * 0.2
bg_bgr = cmyk_to_bgr(bg_C, bg_M, bg_Y, bg_K)
bg = (bg_bgr[1:1])
src = np.zeros((h, w, 3), np.uint8) * 255

# 白日：正白色
cy = bg_src.shape[0] // 2
cx = bg_src.shape[1] // 2
white = (255, 255, 255)
wh_cr = bg_src.shape[1] // 8
bg_cr = wh_cr * 3
cv2.circle(src, (cx, cy), bg_cr, bg, -1)
cv2.circle(src, (cx, cy), wh_cr, white, -1)

# w_C, bg_M, bg_Y, bg_K = bgr_cmyk(bg_src)
# bg_C = np.ones_like(bg_C) * 1.0
# bg_M = np.ones_like(bg_M) * 0.8
# bg_Y = np.zeros_like(bg_Y) * 0.0
# bg_K = np.ones_like(bg_K) * 0.2
# bg_bgr = cmyk_to_bgr(bg_C, bg_M, bg_Y, bg_K)

cv2.imshow('cmyk', src)
cv2.waitKey(0)
cv2.destroyAllWindows()
