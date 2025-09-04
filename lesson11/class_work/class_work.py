# Hu 矩
# 輪廓匹配
import cv2


def hu_moment(src):
    # 輪廓檢測
    src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

    # 二值化
    _, dst_binary = cv2.threshold(src_gray, 127, 255,
                                  cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    contours, _ = cv2.findContours(dst_binary,
                                   cv2.RETR_LIST,
                                   cv2.CHAIN_APPROX_SIMPLE)
    # 創建一個空列表，用於儲存所有輪廓的面積
    areas = []
    for contour in contours:
        areas.append(cv2.contourArea(contour))

    # 檢查是否有輪廓
    if not areas:
        print("沒有找到任何輪廓。")
    else:
        # 找到最大的輪廓面積作為參考
        max_area = max(areas)

        # 設定面積篩選的百分比範圍
        # 這裡的範例是篩選出面積大於最大面積 70% 的所有輪廓
        min_area_threshold = max_area * 0.7

        # 建立一個列表，用於儲存符合條件的輪廓
        similar_contours = []

        # 遍歷所有輪廓，篩選出面積相近的輪廓
        for i, contour in enumerate(contours):
            if areas[i] >= min_area_threshold:
                similar_contours.append(contour)

    return similar_contours


src = cv2.imread("template.jpg")
src1 = cv2.imread("exercise2.jpg")
cv2.imshow("src", src)
cv2.imshow("src1", src1)

contours = hu_moment(src)
contours1 = hu_moment(src1)
# 繪製文字
font = cv2.FONT_HERSHEY_SIMPLEX
n = len(contours1)
for i in range(n):
    cv2.putText(src1, str(i), contours1[i][0][0], font, 1, (0, 0, 255), 2)
cv2.imshow("result", src1)
# 輪廓匹配
for j in range(n):
    match = cv2.matchShapes(contours[0], contours1[j], 3, 0.0)
    print(f"輪廓{j}相比對結果為 = {match}")
    if match >= 0.3:
        dst = cv2.drawContours(src1, contours1[j], -1, (0, 255, 0), -1)
        cv2.imshow("result", dst)
        print(match)
    else:
        print("無符合圖樣")
cv2.waitKey(0)
cv2.destroyAllWindows()
