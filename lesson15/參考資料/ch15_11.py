import cv2

video = cv2.VideoCapture('iceocean.mov')    # 開啟影片檔案
while (video.isOpened()):
    ret, frame = video.read()               # 讀取影片檔案
    if ret:
        cv2.namedWindow('myVideo', 0)
        cv2.resizeWindow('myVideo', 300, 200)
        cv2.imshow('myVideo', frame)        # 顯示影片
    else:
        break
    c = cv2.waitKey(50)                     # 可以控制撥放速度
    if c == 27:                             # 若按 Esc 鍵, 結束
        break
video.release()                             # 關閉輸出物件
cv2.destroyAllWindows()
