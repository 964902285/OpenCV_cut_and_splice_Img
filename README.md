# OpenCV_cut_and_splice_Img

## 踩坑：
### 1、OpenCV 版本问题：如，使用surf or xfeatures2d 报错
### 2、输入图片尺寸问题：如，ValueError: could not broadcast input array from shape (130,130,3) into shape (128,128,3)
## 解决：
### 1、更换版本，目前我使用的版本为：pip install opencv-python==3.4.6.27，pip install opencv-contrib-python==3.4.2.17
### 2、修改输入图片尺寸，如高（行）要一致
