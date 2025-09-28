import cv2

capture = cv2.VideoCapture(0)           # 初始化攝影功能
while (capture.isOpened()):
    ret, frame = capture.read()         # 讀取攝影機的影像
    cv2.imshow('Frame', frame)          # 顯示彩色影像
    h_frame = cv2.flip(frame, 1)        # 水平翻轉
    cv2.imshow('Flip Frame', h_frame)   # 顯示水平翻轉
    c = cv2.waitKey(1)                  # 等待時間 1 毫秒
    if c == 27:                         # 若按 Esc 鍵, 結束
        break
capture.release()                       # 關閉攝影功能
cv2.destroyAllWindows()
