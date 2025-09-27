# 人臉偵測
import cv2

pictPath_face = r'C:\Users\q5j6j\miniconda3\envs\opencv-new\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml'
pictPath_lefteye = r'C:\Users\q5j6j\miniconda3\envs\opencv-new\Lib\site-packages\cv2\data\haarcascade_lefteye_2splits.xml'
pictPath_righteye = r'C:\Users\q5j6j\miniconda3\envs\opencv-new\Lib\site-packages\cv2\data\haarcascade_righteye_2splits.xml'
face_cascade = cv2.CascadeClassifier(pictPath_face)
lefteye_cascade = cv2.CascadeClassifier(pictPath_lefteye)
righteye_cascade = cv2.CascadeClassifier(pictPath_righteye)
# 建立辨識物件
img = cv2.imread("leclerc.png") 
# 讀取影像
faces = face_cascade.detectMultiScale(img, scaleFactor=1.1,
                                      minNeighbors=3, minSize=(20, 20))
lefteyes = lefteye_cascade.detectMultiScale(img, scaleFactor=1.1,
                                            minNeighbors=1, minSize=(5, 5))
righteyes = righteye_cascade.detectMultiScale(img, scaleFactor=1.1,
                                              minNeighbors=1, minSize=(5, 5))
# 標註右下角底色是黃色
cv2.rectangle(img, (img.shape[1]-140, img.shape[0]-20),
              (img.shape[1], img.shape[0]), (0, 255, 255), -1)
# 標註找到多少的人臉
cv2.putText(img, "Finding " + str(len(faces)) + " face",
            (img.shape[1]-135, img.shape[0]-5),
            cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0), 1)
# 將人臉框起來, 由於有可能找到好幾個臉所以用迴圈繪出來
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)  # 藍色框住人臉
    for (x1, y1, w1, h1) in lefteyes:
        cv2.circle(img, (int(x1+w1/2), int(y1+h1/2)),
                   int(h1/2), (0, 255, 0), 2)    # 左眼綠色畫圓
        for (x2, y2, w2, h2) in righteyes:
            cv2.circle(img, (int(x2+w2/2), int(y2+h2/2)),
                       int(h2/2), (0, 0, 255), 2)    # 右眼紅色畫圈
cv2.imshow("Face", img)
# 儲存影像檔
cv2.imwrite("leclerc_eyes.jpg", img)
# 顯示影像
cv2.waitKey(0)
cv2.destroyAllWindows()
