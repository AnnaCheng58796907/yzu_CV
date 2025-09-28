import cv2

capture = cv2.VideoCapture(0)                               # 初始化攝影功能
while (capture.isOpened()):
    ret, frame = capture.read()                             # 讀取攝影機的影像
    cv2.imshow('Frame', frame)                              # 顯示彩色影像
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)    # 轉灰階顯示
    cv2.imshow('Gray Frame', gray_frame)                    # 顯示灰階影像
    c = cv2.waitKey(1)                                      # 等待時間 1 毫秒
    if c == 27:                                             # 若按 Esc 鍵, 結束
        break
capture.release()                                           # 關閉攝影功能
cv2.destroyAllWindows()
