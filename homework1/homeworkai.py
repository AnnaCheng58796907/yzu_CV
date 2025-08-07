import cv2
import numpy as np


def add_value_with_clip(two_array: np.ndarray, max_val: int) -> np.ndarray:
    """
    將陣列數值增加 5，並使用 np.clip() 確保數值在 [0, max_val] 範圍內。
    """
    two_array[:] = np.clip(two_array.astype(np.int16) + 5, 0, max_val)
    two_array.astype(np.uint8)
    return two_array


def reduce_value_with_clip(two_array: np.ndarray, max_val: int) -> np.ndarray:
    """
    將陣列數值減少 5，並使用 np.clip() 確保數值在 [0, max_val] 範圍內。
    """
    two_array[:] = np.clip(two_array.astype(np.int16) - 5, 0, max_val)
    two_array.astype(np.uint8)
    return two_array


def main() -> None:
    img = cv2.imread('street.jpg')
    if img is None:
        print("錯誤: 無法讀取影像檔。請確認 'street.jpg' 檔案是否存在。")
        return

    original_img = img.copy()

    cv2.namedWindow('street', cv2.WINDOW_NORMAL)
    cv2.imshow('street', img)

    print("使用鍵盤按鍵調整影像：")
    print("w: 色相+5, s: 色相-5")
    print("e: 飽和度+5, d: 飽和度-5")
    print("r: 明度+5, f: 明度-5")
    print("y: 重設影像, q: 關閉視窗")

    # 在迴圈外進行第一次 HSV 轉換
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv_img)

    while True:
        ret_value = cv2.waitKey(0)

        if ret_value == ord('q'):
            break

        # 根據按鍵調整對應的 HSV 通道
        if ret_value == ord('w'):
            h = add_value_with_clip(h, 179)
        elif ret_value == ord('s'):
            h = reduce_value_with_clip(h, 179)
        elif ret_value == ord('e'):
            s = add_value_with_clip(s, 255)
        elif ret_value == ord('d'):
            s = reduce_value_with_clip(s, 255)
        elif ret_value == ord('r'):
            v = add_value_with_clip(v, 255)
        elif ret_value == ord('f'):
            v = reduce_value_with_clip(v, 255)
        elif ret_value == ord('y'):
            # 重設為原始影像的 HSV
            hsv_img = cv2.cvtColor(original_img, cv2.COLOR_BGR2HSV)
            h, s, v = cv2.split(hsv_img)
        else:
            continue
        merged_hsv = cv2.merge([h, s, v])
        img = cv2.cvtColor(merged_hsv, cv2.COLOR_HSV2BGR)
        cv2.imshow('street', img)

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
