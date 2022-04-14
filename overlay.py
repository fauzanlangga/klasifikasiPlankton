import cv2
import os
import numpy as np


rgbPath = r"D:\Magang\Lipi\Train\Jakarta Bay 2019-instance-segmentation\Jakarta Bay 2019\img\Plankton (130).jpg"
bwPath = r"D:\Magang\Lipi\Train\Jakarta Bay 2019-instance-segmentation\Jakarta Bay 2019\result0\Plankton (130).jpg"
#overlayPath = r"D:\Magang\"




rgb = cv2.imread(rgbPath)
bw = cv2.imread(bwPath)


M = bw.shape[0]
N = bw.shape[1]

seg = np.zeros((M, N, 3), np.uint8)

for i in range(M):
    for j in range(N):
        if bw[i,j,0] == 255:
            for k in range(1):
                rgb[i,j,k] = seg[i,j,k]


def rescaleFrame(frame, scale=0.3):
    #berfungsi untuk gambar, video dan live video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width,height)

    return cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)
resize_image = rescaleFrame(rgb)

#cv2.imshow("rgb", rgb)
#cv2.imshow("bw", bw)
cv2.imshow("SEG", resize_image)
#cv2.imwrite("D:\Magang\images.jpg", rgb)
#cv2.imwrite(overlayPath + item, rgb)
print('success write overlay ')


cv2.waitKey(0)
cv2.destroyAllWindows()