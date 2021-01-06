import cv2
import numpy as np

img = cv2.imread("imgs\\2.png")
print(img.shape)  # 高度、宽度、通道数。一张图片基本都是一个三维数组：行，列，通道数，切片只是涉及到前两维
# cropped = img[0:128, 0:512]  # 裁剪坐标为[y0:y1, x0:x1]
AOI_img = img[0:375, 240:480]
cv2.imwrite("imgs\\cv_AOI_thor.jpg", AOI_img)
