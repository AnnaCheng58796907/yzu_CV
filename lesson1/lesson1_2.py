import cv2

img = cv2.imread('coca-cola-logo.png')

# 觀察回傳的資料型態
print(type(img))

# 觀察回穿的資料內容
print(img)

# 觀察回傳的資料形狀
print(img.shape)