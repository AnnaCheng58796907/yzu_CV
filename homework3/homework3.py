import cv2
import numpy as np


def bgr_cmyk(img) -> np.ndarray:
    # bgr轉換cmyk
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


def end_points(center, length, angle_deg):
    # 繪製30度尖角
    angle_rad = np.deg2rad(angle_deg)
    x = int(center[0] + length * np.cos(angle_rad))
    y = int(center[1] - length * np.sin(angle_rad))
    return (x, y)


red_w = 900
red_h = int((red_w * 2) / 3)

# 紅地：CMYK (0%, 100%, 100%, 10%)
red_src = np.ones((red_h, red_w, 4), np.uint8) * 255
C, M, Y, K = bgr_cmyk(red_src)
red_C = np.zeros_like(C) * 0.0
red_M = np.ones_like(M) * 1.0
red_Y = np.ones_like(Y) * 1.0
red_K = np.ones_like(K) * 0.1
red_src = cmyk_to_bgr(red_C, red_M, red_Y, red_K)

# 青天：CMYK (100%, 80%, 0%, 20%)
bg_C = np.ones_like(C) * 1.0
bg_M = np.ones_like(M) * 0.8
bg_Y = np.zeros_like(Y) * 0.0
bg_K = np.ones_like(K) * 0.2
bg_src = cmyk_to_bgr(bg_C, bg_M, bg_Y, bg_K)
bg_src = cv2.resize(bg_src, None, fx=0.5, fy=0.5)


# 白日：正白色
cy = bg_src.shape[0] // 2
cx = bg_src.shape[1] // 2
center_c = (cx, cy)
white = (255, 255, 255)
wh_cr = bg_src.shape[1] // 8
bg_cr = wh_cr * 3
cv2.circle(bg_src, center_c, wh_cr, white, -1)


# 12道光芒
length = wh_cr * 2
angle_deg = 30 // 2

num_angle = 12
angle_step = 360 // num_angle

# 旋轉繪製12道光芒
for i in range(num_angle):
    ba_an = i * angle_step
    # 第1頂點
    firs_point = end_points(center_c, length, ba_an)

    end1_angle = ba_an + 180 - angle_deg
    end2_angle = ba_an + 180 + angle_deg

    pts1 = end_points(firs_point, length, end1_angle)
    pts2 = end_points(firs_point, length, end2_angle)

    pts = np.array([firs_point, pts1, pts2], dtype=np.int32)
    pts = pts.reshape(-1, 1, 2)

    cv2.fillPoly(bg_src, [pts], white)


# 青底圓形
bg_b, bg_g, bg_r = bg_src[1, 1]
bg_color = (int(bg_b), int(bg_g), int(bg_r))
bg_rw = (wh_cr * 2) // 15
bg_cr = wh_cr + (bg_rw // 2)
cv2.circle(bg_src, center_c, bg_cr, bg_color, bg_rw)

# 國旗合併
h, w = bg_src.shape[:2]
red_src[0:h, 0:w] = bg_src

cv2.imshow('Flag of the Republic of China', red_src)
cv2.waitKey(0)
cv2.destroyAllWindows()
