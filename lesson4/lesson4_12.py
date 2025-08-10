import cv2

src1 = cv2.imread("lake.jpg")
cv2.imshow("lake", src1)

src2 = cv2.imread("geneva.jpg")
cv2.imshow("geneva.jpg", src2)

alpha = 1
beta = 0.2
gamma = 1

dst = cv2.addWeighted(src1, alpha, src2, beta, gamma)
cv2.imshow("lake+geneva", dst)
cv2.waitKey()
cv2.destroyAllWindows()
