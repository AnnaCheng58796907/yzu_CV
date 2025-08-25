import cv2
import numpy as np


def mask_contours(src1):
    # 尋找最大輪廓的四邊頂點
    # 將圖像轉為灰階
    gray = cv2.cvtColor(src1, cv2.COLOR_BGR2GRAY)
    # 進行二值化，將物體變為白色，背景變為黑色
    _, binary = cv2.threshold(gray, 73, 255, cv2.THRESH_BINARY)
    # 尋找輪廓
    contours, _ = cv2.findContours(binary,
                                   cv2.RETR_EXTERNAL,
                                   cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        # 找到面積最大的輪廓
        largest_contour = max(contours, key=cv2.contourArea)

        # 計算輪廓的周長
        perimeter = cv2.arcLength(largest_contour, True)

        # 使用 approxPolyDP 簡化輪廓，嘗試找到四個頂點
        epsilon = 0.04 * perimeter
        approx_poly = cv2.approxPolyDP(largest_contour, epsilon, True)

        # 確保我們找到的是一個四邊形
        if len(approx_poly) == 4:
            # 將 numpy 陣列重塑為 (4, 2)
            box = approx_poly.reshape(4, 2)

            # ------------------- 關鍵步驟：對頂點進行排序 -------------------

            # 創建一個空的 numpy 陣列來存放排序後的頂點
            sorted_points = np.zeros((4, 2), dtype=np.int32)

            # 1. 根據 x + y 的總和排序，找到左上角和右下角的點
            s = box.sum(axis=1)
            sorted_points[0] = box[np.argmin(s)]  # 總和最小的是左上角
            sorted_points[2] = box[np.argmax(s)]  # 總和最大的是右下角

            # 2. 根據 x - y 的差值排序，找到右上角和左下角的點
            d = np.diff(box, axis=1)
            sorted_points[1] = box[np.argmin(d)]  # 差值最小的是左下角
            sorted_points[3] = box[np.argmax(d)]  # 差值最大的是右上角

        else:
            print("簡化後的輪廓不是一個四邊形。請嘗試調整 epsilon。")
    else:
        print("沒有找到任何輪廓。")

    return sorted_points


def mask_src(src1, src2, sorted_points):
    # 將找到的不規則四邊形的四個頂點，儲存在 approx_poly 中
    # approx_poly 應該是一個形狀為 (4, 1, 2) 的 numpy 陣列
    # 為了後續處理，我們將其重塑為 (4, 2)
    # 確保頂點順序是正確的 (例如: 左上, 右上, 右下, 左下)
    # 以下是一個假設的 approx_poly，替換成你實際找到的頂點
    approx_poly = np.array([sorted_points], dtype=np.float32)
    pts1 = approx_poly.reshape(4, 2)

    # 獲取目標圖片的尺寸
    h_target, w_target = src2.shape[:2]

    # 定義目標圖片的對應頂點 (通常是四個角落)
    # 注意順序要和原始圖片的四邊形頂點對應
    pts2 = np.float32([[0, 0],
                       [w_target, 0],
                       [w_target, h_target],
                       [0, h_target]])

    # 計算透視變換矩陣
    M = cv2.getPerspectiveTransform(pts2, pts1)

    # 應用透視變換到目標圖片
    # 使用原始圖片的大小作為輸出大小，這樣變形後的圖片會覆蓋整個原始圖片
    warped_image = cv2.warpPerspective(src2, M,
                                       (src1.shape[:2][1],
                                        src1.shape[:2][0]))

    # 創建一個遮罩，只在不規則四邊形內部為白色
    mask = np.zeros(src1.shape[:2], dtype=np.uint8)
    cv2.fillPoly(mask, [pts1.astype(np.int32)], 255)

    # 將遮罩擴展到三個通道，以用於彩色圖像的按位與操作
    mask_inv = cv2.bitwise_not(mask)
    mask_color = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    mask_inv_color = cv2.cvtColor(mask_inv, cv2.COLOR_GRAY2BGR)

    # 使用遮罩將原始圖片中四邊形區域變為黑色
    original_masked = cv2.bitwise_and(src1, mask_inv_color)

    # 使用遮罩將變形後的目標圖片的內容放到對應區域
    warped_masked = cv2.bitwise_and(warped_image, mask_color)

    # 將兩部分圖像相加，得到最終結果
    result = cv2.add(original_masked, warped_masked)

    return result


def main():
    src1 = cv2.imread("image1_1.jpg")
    src1 = cv2.resize(src1, None, fx=0.3, fy=0.3)
    src2 = cv2.imread("geneva.jpg")

    # 尋找原圖內灰階閾值處理後，找到最大面積輪廓的四個頂點
    sorted_points = mask_contours(src1)

    # 將原圖與要替換的圖片做遮罩及變形替換
    image2 = mask_src(src1, src2, sorted_points)

    cv2.imshow("image1", src1)
    cv2.imshow("image2", image2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
