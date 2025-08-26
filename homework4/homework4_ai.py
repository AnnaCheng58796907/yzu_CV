import cv2
import numpy as np


def find_quadrilateral_vertices(image):
    """
    尋找圖像中最大輪廓的四邊形頂點。

    Args:
        image: 原始彩色圖像。

    Returns:
        一個 (4, 2) 的 numpy 陣列，包含排序後的四個頂點，
        順序為左上、右上、右下、左下。如果沒有找到，則回傳 None。
    """
    # 將圖像轉為灰階
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # --- 回歸你最原始且有效的固定閾值方法 ---
    # 使用固定的 73 進行二值化，這對你的特定圖片效果最好
    _, binary = cv2.threshold(gray, 73, 255, cv2.THRESH_BINARY)

    # 尋找輪廓
    contours, _ = cv2.findContours(binary,
                                   cv2.RETR_EXTERNAL,
                                   cv2.CHAIN_APPROX_SIMPLE)

    if not contours:
        print("沒有找到任何輪廓。")
        return None

    # 找到面積最大的輪廓
    largest_contour = max(contours, key=cv2.contourArea)

    '''
    cv2.arcLength: 是OpenCV中用來計算曲線或輪廓周長（或弧長）的函數。
    它接受兩個參數：一個是輸入的輪廓（通常是由cv2.findContours返回的點集），
                  另一個是布林值closed，用來指定該曲線是否封閉。
                    若是封閉輪廓（例如多邊形），closed設為True；
                    若是開放曲線（例如線段），closed設為False。
        該函數會計算點集中相鄰點之間的距離總和，返回輪廓的周長或曲線的弧長。

    cv2.approxPolyDP是OpenCV中用來對曲線或多邊形進行「多邊形逼近」的函數。
    它基於Douglas-Peucker演算法，能用更少的頂點去逼近原始曲線，
    使得逼近曲線與原始曲線之間的最大距離不超過指定的精度參數epsilon。
    這個函數的主要參數包括：
        curve：輸入的2D點集，通常是輪廓的點。
        epsilon：逼近精度的最大距離值，越小代表逼近越精確，但頂點數越多。
        closed：布林值，表示該曲線是否封閉，True表示首尾相連閉合。
    函數返回逼近後的多邊形點集，其頂點數通常比原始輪廓少，適用於形狀簡化、輪廓分析等場景。
    '''
    # --- 保留動態調整 epsilon 的邏輯，以確保找到四個頂點 ---
    perimeter = cv2.arcLength(largest_contour, True)

    for epsilon_factor in np.linspace(0.1, 0.01, num=20):
        epsilon = epsilon_factor * perimeter
        approx_poly = cv2.approxPolyDP(largest_contour, epsilon, True)

        if len(approx_poly) == 4:
            vertices = approx_poly.reshape(4, 2)
            s = vertices.sum(axis=1)
            sorted_vertices = np.zeros((4, 2), dtype=np.float32)
            sorted_vertices[0] = vertices[np.argmin(s)]
            sorted_vertices[2] = vertices[np.argmax(s)]

            d = np.diff(vertices, axis=1)
            sorted_vertices[1] = vertices[np.argmin(d)]
            sorted_vertices[3] = vertices[np.argmax(d)]

            print(f"成功找到四邊形！使用的 epsilon_factor: {epsilon_factor:.2f}")
            return sorted_vertices

    # 如果循環結束後仍未找到四邊形，回傳 None
    print(f"未能找到四邊形，簡化後的頂點數為 {len(approx_poly)}。請手動調整 epsilon。")
    return None


def apply_perspective_transform(src_image, target_image, vertices):
    """
    將目標圖片進行透視變換並嵌入到原始圖片的指定區域。
    """
    if vertices is None:
        return None

    pts1 = vertices.astype(np.float32)

    h_target, w_target = target_image.shape[:2]

    pts2 = np.float32([[0, 0],
                       [w_target - 1, 0],
                       [w_target - 1, h_target - 1],
                       [0, h_target - 1]])

    M = cv2.getPerspectiveTransform(pts2, pts1)

    warped_image = cv2.warpPerspective(target_image, M,
                                       (src_image.shape[1],
                                        src_image.shape[0]))

    mask = np.zeros(src_image.shape[:2], dtype=np.uint8)
    cv2.fillPoly(mask, [pts1.astype(np.int32)], 255)

    mask_inv = cv2.bitwise_not(mask)

    original_masked = cv2.bitwise_and(src_image, src_image, mask=mask_inv)

    warped_masked = cv2.bitwise_and(warped_image, warped_image, mask=mask)

    result = cv2.add(original_masked, warped_masked)

    return result


def main():
    """
    主函式，執行圖片讀取、處理和顯示。
    """
    src1 = cv2.imread("image1_1.jpg")
    src2 = cv2.imread("geneva.jpg")

    if src1 is None or src2 is None:
        print("錯誤：無法讀取圖片，請檢查檔案路徑。")
        return

    src1 = cv2.resize(src1, None, fx=0.3, fy=0.3)

    sorted_vertices = find_quadrilateral_vertices(src1)

    final_image = apply_perspective_transform(src1, src2, sorted_vertices)

    if final_image is not None:
        cv2.imshow("Original Image", src1)
        cv2.imshow("Final Image", final_image)
        cv2.imwrite("image2_optimized.jpg", final_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
