import numpy as np
import json
import os
import cv2

rgbPath = "D:/rgb to bw/rgb/"
jsonPath = "D:/rgb to bw/ann/"
#bwPath = "D:/Magang/Lipi"

#mengambil path json
jsonFiles = os.listdir(jsonPath)

#mengambil path rgb
rgbFiles = os.listdir(rgbPath)

#mengambil file rgb
img0 = cv2.imread(os.path.join(rgbPath,rgbFiles[0]))

#mengambil width dan height
height = img0.shape[0]
width = img0.shape[1]

for item in jsonFiles:
    #menambahkan background
    img = np.zeros((height, width, 3), dtype = "uint8")
    # print(item)
 
    #buka file json
    jsonf = open(os.path.join(jsonPath,item))

    #parsing data json
    data = json.loads(jsonf.read())

    #mengambil points yang ada di json
    point = []
    for points in data['objects'][1]['points']['exterior']:
        point.append(points)

    #membuat polygon dari points
    polygon = np.array(point, np.int32)

    #membuat polygon warna putih dalam background gambar
    polyImage = cv2.fillConvexPoly(img, polygon, (255,255,255))

    
    def rescaleFrame(frame, scale=0.1):
        #berfungsi untuk gambar, video dan live video
        lebar = int(frame.shape[1] * scale)
        tinggi = int(frame.shape[0] * scale)

        dimensions = (lebar,tinggi)

        return cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)
    resize_image = rescaleFrame(polyImage)
    asli = rescaleFrame(img0)

    #menampilkan gambar
    #cv2.imshow("RGB", asli)
    cv2.imshow("BW", resize_image)

    #memberi nama untuk bw jpg, dengan mengurangi 5 huruf terakhir dari json file
    bwFile = item[:-5]

    #cv2.imwrite(bwPath + bwFile, img)

    #print(bwFile + " berhasil ditambahkan")

    cv2.waitKey(0)
    cv2.destroyAllWindows()