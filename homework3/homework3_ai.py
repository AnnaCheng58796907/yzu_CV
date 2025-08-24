import cv2
import numpy as np


def bgr_cmyk(img: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """
    將 BGR 圖像轉換為 CMYK 色彩空間。
    參數:
        img (np.ndarray): BGR 格式的圖像陣列。
    回傳值:
        tuple: 包含 C, M, Y, K 四個通道的 NumPy 陣列。
    """
    # 將 BGR 數值正規化到 0.0 到 1.0 的範圍
    bgr_norm = img.astype(float) / 255.0

    # 計算 K (Key/Black) 通道
    # K = 1 - max(R, G, B)
    K = 1 - np.max(bgr_norm, axis=2)

    # 為了避免除以零，設定一個最小閾值
    denominator = 1 - K
    denominator[denominator == 0] = 1e-10

    # 根據公式計算 C, M, Y 通道
    C = (1 - bgr_norm[..., 2] - K) / denominator
    M = (1 - bgr_norm[..., 1] - K) / denominator
    Y = (1 - bgr_norm[..., 0] - K) / denominator

    return C, M, Y, K


def cmyk_to_bgr(C: np.ndarray, M: np.ndarray, Y: np.ndarray, K: np.ndarray) -> np.ndarray:
    """
    將 CMYK 通道轉換為 BGR 圖像。
    參數:
        C, M, Y, K (np.ndarray): CMYK 四個通道的 NumPy 陣列。
    回傳值:
        np.ndarray: BGR 格式的圖像陣列。
    """
    # 根據公式計算 B, G, R 通道
    B = (1 - Y) * (1 - K) * 255
    G = (1 - M) * (1 - K) * 255
    R = (1 - C) * (1 - K) * 255
    
    # 將三個通道堆疊成一個 BGR 圖像陣列，並轉換為 np.uint8 格式
    bgr = np.stack([B, G, R], axis=-1).astype(np.uint8)
    return bgr


# --- 國旗繪製主程式 ---
def draw_roc_flag(width: int) -> np.ndarray:
    """
    根據指定的寬度，繪製中華民國國旗。
    
    此函式嚴格遵守以下 13 項條件：
    1. 圓形青白色。
    2. 白日居中，並有十二道白尖角光芒。
    3. 白日與十二道白尖角光芒間，留一青色圓圈。
    4. 青底圓形之圓心為白日體之圓心。
    5. 白日體半徑與青底圓形半徑為一與三之比。
    6. 白日體圓心至白尖角光芒頂，其長度與白日體半徑，為二與一之比。
    7. 白日與十二道白尖角光芒間之青圈，其寬度等於白日體直徑十五分之一。
    8. 每道白尖角光芒之頂角為三十度，十二角為三百六十度。
    9. 白尖角光芒之上下左右排列應正對北南西東方向，其餘均勻排列。
    10. 旗面之橫度與縱度為三與二之比。
    11. 青天為長方形，其面積為全旗之四分之一。
    12. 長方形之青天中置國徽上之白日青圈及十二道白尖角光芒，其白日體圓心位於長方形青天縱橫平分線之交點上。
    13. 白日體半徑與青色長方形之橫長為一與八之比。
    """
    # 10. 旗面之橫度與縱度為三與二之比
    height = int(width * 2 / 3)

    # 11. 青天為長方形，其面積為全旗之四分之一
    canton_width = int(width / 2)
    canton_height = int(height / 2)

    # 13. 白日體半徑與青色長方形之橫長為一與八之比
    white_sun_radius = int(canton_width / 8)
    
    # 5. 白日體半徑與青底圓形半徑為一與三之比
    blue_circle_radius = white_sun_radius * 3

    # 6. 白日體圓心至白尖角光芒頂，其長度與白日體半徑，為二與一之比
    ray_tip_length = white_sun_radius * 2

    # 7. 白日與十二道白尖角光芒間之青圈，其寬度等於白日體直徑十五分之一
    blue_ring_width = int((white_sun_radius * 2) / 15)

    # 國旗的 CMYK 顏色定義
    # 紅地：CMYK (0%, 100%, 100%, 10%)
    c_red, m_red, y_red, k_red = 0, 1, 1, 0.1
    # 青天：CMYK (100%, 80%, 0%, 20%)
    c_blue, m_blue, y_blue, k_blue = 1, 0.8, 0, 0.2

    # 創建紅地圖像
    red_field_cmyk = np.full((height, width, 4), [c_red, m_red, y_red, k_red], dtype=np.float32)
    flag_image = cmyk_to_bgr(red_field_cmyk[..., 0], red_field_cmyk[..., 1],
                             red_field_cmyk[..., 2], red_field_cmyk[..., 3])

    # 創建青天圖像 (長方形)
    blue_canton_cmyk = np.full((canton_height, canton_width, 4), [c_blue, m_blue, y_blue, k_blue], dtype=np.float32)
    blue_canton = cmyk_to_bgr(blue_canton_cmyk[..., 0], blue_canton_cmyk[..., 1],
                              blue_canton_cmyk[..., 2], blue_canton_cmyk[..., 3])

    # 12. 白日體圓心位於長方形青天縱橫平分線之交點上
    center_y, center_x = blue_canton.shape[0] // 2, blue_canton.shape[1] // 2
    
    # 2. 白日居中，並有十二道白尖角光芒
    # 在青天上繪製白日
    cv2.circle(blue_canton, (center_x, center_y), white_sun_radius, (255, 255, 255), -1)

    # 繪製 12 道光芒
    num_rays = 12
    # 8. 每道白尖角光芒之頂角為三十度
    ray_angle_half = 30 / 2  # 光芒的半角
    
    # 9. 白尖角光芒之上下左右排列應正對北南西東方向，其餘均勻排列
    angle_step = 360 / num_rays
    
    for i in range(num_rays):
        # 計算光芒的中心線角度
        current_angle = i * angle_step
        
        # 計算光芒尖端點
        tip_x = int(center_x + ray_tip_length * np.cos(np.deg2rad(current_angle)))
        tip_y = int(center_y - ray_tip_length * np.sin(np.deg2rad(current_angle)))

        # 計算光芒基部所在的兩個點 (位於白日體圓周上)
        base1_x = int(center_x + white_sun_radius * np.cos(np.deg2rad(current_angle + ray_angle_half)))
        base1_y = int(center_y - white_sun_radius * np.sin(np.deg2rad(current_angle + ray_angle_half)))
        
        base2_x = int(center_x + white_sun_radius * np.cos(np.deg2rad(current_angle - ray_angle_half)))
        base2_y = int(center_y - white_sun_radius * np.sin(np.deg2rad(current_angle - ray_angle_half)))
        
        # 創建頂點陣列，並繪製填充多邊形（三角形）
        ray_points = np.array([(tip_x, tip_y), (base1_x, base1_y), (base2_x, base2_y)])
        cv2.fillPoly(blue_canton, [ray_points], (255, 255, 255))

    # 3. 白日與十二道白尖角光芒間，留一青色圓圈
    # 4. 青底圓形之圓心為白日體之圓心
    # 7. 青圈其寬度等於白日體直徑十五分之一
    blue_color_bgr = blue_canton[1, 1]
    cv2.circle(blue_canton, (center_x, center_y), white_sun_radius + blue_ring_width, 
               (int(blue_color_bgr[0]), int(blue_color_bgr[1]), int(blue_color_bgr[2])), blue_ring_width)
    
    # 將青天圖案放置到紅地圖像上
    flag_image[0:canton_height, 0:canton_width] = blue_canton

    return flag_image


# --- 主程式執行區塊 ---
if __name__ == "__main__":
    # 設定國旗寬度，可自行調整
    flag_width = 900
    # 呼叫函式繪製國旗
    flag = draw_roc_flag(flag_width)

    # 顯示國旗圖像
    cv2.imshow('Flag of the Republic of China', flag)
    # 等待任意按鍵，然後關閉視窗
    cv2.waitKey(0)
    cv2.destroyAllWindows()
