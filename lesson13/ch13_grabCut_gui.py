import cv2
import numpy as np
import os

# 嘗試用檔案對話框選圖（無視窗環境會自動退回預設路徑）


def choose_image_path(default_path="lena.jpg"):
    try:
        import tkinter as tk
        from tkinter import filedialog
        root = tk.Tk()
        root.withdraw()
        path = filedialog.askopenfilename(
            title="選擇影像",
            filetypes=[("Images", "*.jpg *.jpeg *.png *.bmp *.tif *.tiff"),
                       ("All files", "*.*")])
        root.destroy()
        if path:
            return path
    except Exception:
        pass
    return default_path


# 顏色與 GrabCut 標籤
BLUE = (255,   0,   0)  # 矩形框線
RED = (0,   0, 255)  # 確定前景筆刷顏色（畫在畫面上）
GREEN = (0, 255,   0)  # 確定背景筆刷顏色
LIGHT_RED = (100, 100, 255)  # 可能前景
LIGHT_GREEN = (100, 255, 100)  # 可能背景

# GrabCut 的標籤值
BGD = 0  # 確定背景
FGD = 1  # 確定前景
PR_BGD = 2  # 可能背景
PR_FGD = 3  # 可能前景

colors = {BGD: GREEN, FGD: RED, PR_BGD: LIGHT_GREEN, PR_FGD: LIGHT_RED}
labels_name = {
    BGD: "Background(0)",
    FGD: "Foreground(1)",
    PR_BGD: "Prob. BG(2)",
    PR_FGD: "Prob. FG(3)"
}


class GrabCutGUI:
    def __init__(self, img):
        self.img0 = img
        self.img = img.copy()
        self.mask = np.full(img.shape[:2], PR_BGD, np.uint8)  # 初始全設為可能背景，較穩定
        self.output = np.zeros_like(img)

        self.brush_radius = 6
        self.drawing = False
        self.mode = FGD  # 預設畫前景
        self.rect = (0, 0, 1, 1)
        self.rect_or_mask = 0   # 0: 未用rect或mask初始化，1: 用rect，2: 用mask
        self.rect_over = False
        self.rect_endpoint_tmp = []

        self.bgModel = np.zeros((1, 65), np.float64)
        self.fgModel = np.zeros((1, 65), np.float64)

        self.win = "GrabCut Painter"
        cv2.namedWindow(self.win)
        cv2.setMouseCallback(self.win, self.onmouse)

    def onmouse(self, event, x, y, flags, param):
        # 右鍵：畫矩形
        if event == cv2.EVENT_RBUTTONDOWN:
            self.rect_or_mask = 0
            self.rect_over = False
            self.rect = (x, y, 1, 1)
            self.rect_endpoint_tmp = [(x, y)]
        elif event == cv2.EVENT_RBUTTONUP:
            self.rect_endpoint_tmp.append((x, y))
            x0, y0 = self.rect_endpoint_tmp[0]
            x1, y1 = self.rect_endpoint_tmp[1]
            x_min, y_min = min(x0, x1), min(y0, y1)
            x_max, y_max = max(x0, x1), max(y0, y1)
            self.rect = (x_min, y_min, x_max - x_min, y_max - y_min)
            self.rect_over = True
            self.rect_or_mask = 1  # 用Rect初始化
            self.img = self.img0.copy()
            cv2.rectangle(self.img, (x_min, y_min), (x_max, y_max), BLUE, 2)

        # 左鍵：塗鴉筆刷
        if event == cv2.EVENT_LBUTTONDOWN:
            self.drawing = True
            self.draw_brush((x, y))
        elif event == cv2.EVENT_MOUSEMOVE and self.drawing:
            self.draw_brush((x, y))
        elif event == cv2.EVENT_LBUTTONUP:
            self.drawing = False
            self.draw_brush((x, y))

    def draw_brush(self, pt):
        x, y = pt
        cv2.circle(self.img, (x, y), self.brush_radius,
                   colors[self.mode], -1, cv2.LINE_AA)
        cv2.circle(self.mask, (x, y), self.brush_radius,
                   self.mode, -1, cv2.LINE_AA)
        self.rect_or_mask = 2  # 有手繪標註了

    def run_grabcut(self, iter_count=1):
        if self.rect_or_mask == 0 and not self.rect_over:
            return  # 尚未給 rect 或 mask
        if self.rect_or_mask == 1:  # 用矩形初始化
            cv2.grabCut(self.img0, self.mask, self.rect, self.bgModel,
                        self.fgModel, iter_count, cv2.GC_INIT_WITH_RECT)
            self.rect_or_mask = 2  # 之後就用 mask 續跑
        else:  # 用mask續跑
            cv2.grabCut(self.img0, self.mask, None, self.bgModel,
                        self.fgModel, iter_count, cv2.GC_INIT_WITH_MASK)
        self.update_result()

    def update_result(self):
        # 將 PR_FGD 也視為前景以利觀察（可視需要改只顯示確定前景）
        mask2 = np.where((self.mask == FGD) | (
            self.mask == PR_FGD), 255, 0).astype('uint8')
        self.output = cv2.bitwise_and(self.img0, self.img0, mask=mask2)

    def overlay_help(self, canvas):
        help_texts = [
            "Mouse:Left-drag=paint (current brush), Right-drag=draw rectangle",
            "Keys: 0=BG  1=FG  2=Prob. BG  3=Prob. FG",
            "      g=Run GrabCut n=Next iter r=Reset s=Save  +/-=Brush size",
            "      q=Quit",
            f"Brush mode:{labels_name[self.mode]} Radius:{self.brush_radius}"
        ]

        overlay = canvas.copy()
        y = 20
        line_h = 22
        for t in help_texts:
            cv2.putText(overlay, t, (10, y), cv2.FONT_HERSHEY_SIMPLEX,
                        0.3, (30, 30, 30), 3, cv2.LINE_AA)
            cv2.putText(overlay, t, (10, y), cv2.FONT_HERSHEY_SIMPLEX,
                        0.3, (240, 240, 240), 1, cv2.LINE_AA)
            y += line_h
        return overlay

    def show(self):
        while True:
            vis = self.img.copy()
            if self.rect_over:
                x, y, w, h = self.rect
                cv2.rectangle(vis, (x, y), (x+w, y+h), BLUE, 2)
            vis = self.overlay_help(vis)

            # 右側顯示分割結果（併排）
            combined = np.zeros(
                (max(vis.shape[0], self.output.shape[0]),
                 vis.shape[1] + self.output.shape[1], 3),
                dtype=np.uint8)
            combined[:vis.shape[0], :vis.shape[1]] = vis
            combined[:self.output.shape[0],
                     vis.shape[1]:
                     vis.shape[1]+self.output.shape[1]] = self.output
            k = cv2.waitKey(20) & 0xFF

            if k == 27 or k == ord('q'):
                break
            elif k == ord('0'):
                self.mode = BGD
            elif k == ord('1'):
                self.mode = FGD
            elif k == ord('2'):
                self.mode = PR_BGD
            elif k == ord('3'):
                self.mode = PR_FGD
            elif k == ord('g'):
                self.run_grabcut(iter_count=1)
            elif k == ord('n'):
                self.run_grabcut(iter_count=1)
            elif k == ord('r'):
                self.reset()
            elif k == ord('s'):
                self.save_result()
            elif k == ord('+') or k == ord('='):
                self.brush_radius = min(100, self.brush_radius + 1)
            elif k == ord('-') or k == ord('_'):
                self.brush_radius = max(1, self.brush_radius - 1)

        cv2.destroyAllWindows()

    def reset(self):
        self.img = self.img0.copy()
        self.mask[:] = PR_BGD
        self.output[:] = 0
        self.rect = (0, 0, 1, 1)
        self.rect_or_mask = 0
        self.rect_over = False
        self.bgModel[:] = 0
        self.fgModel[:] = 0

    def save_result(self):
        cv2.imwrite("result.png", self.output)
        mask_vis = np.zeros_like(self.img0)
        # 可視化四種標籤
        for lab, col in colors.items():
            mask_vis[self.mask == lab] = col
        cv2.imwrite("mask.png", mask_vis)
        print("Saved: result.png, mask.png")


if __name__ == "__main__":
    path = choose_image_path()
    if not os.path.exists(path):
        raise FileNotFoundError(f"找不到影像：{path}（請換一張圖或把路徑改成你的圖片）")
    img = cv2.imread(path)
    if img is None:
        raise RuntimeError("讀圖失敗，請換一張圖片。")
    app = GrabCutGUI(img)
    app.show()
