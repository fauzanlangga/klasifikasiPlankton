import cv2
import os
import numpy as np


# rgbPath = r"D:/Gambar/kFoldFolders/D0/YDXJ0048 0033/images/YDXJ0048 0033.jpg"
# bwPath = r"D:/Gambar/result1/YDXJ0048 0033.jpg"
# overlayPath = r"D:/Gambar/overlay/"

for kFoldItem in range(1):
    print(kFoldItem)
 
    kFold = kFoldItem

    # if kFold == 0:
    # ### ================= Fold 0 ================
    #     rgbPath = r'C:/Users/fikri/Documents/LIPI Autonomous/kFoldFolders/D3/'   ## fold0 Train: D0-D1-D2  Test: D3
    #     bwPath = r'C:/Users/fikri/Documents/LIPI Autonomous/result/result0_D3/'
    #     overlayPath = 'C:/Users/fikri/Documents/LIPI Autonomous/overlay/overlay0/'   #fold0

    # if kFold == 1:
    # ### ================= Fold 1 ================
    #     rgbPath = r'C:/Users/fikri/Documents/LIPI Autonomous/kFoldFolders/D0/'   ## fold0 Train: D0-D1-D2  Test: D0
    #     bwPath = r'C:/Users/fikri/Documents/LIPI Autonomous/result/result1_D0/'
    #     overlayPath = 'C:/Users/fikri/Documents/LIPI Autonomous/overlay/overlay1/'   #fold1

    # if kFold == 0:
    # ### ================= Fold 2 ================
    #     rgbPath = r'C:/Users/fikri/Documents/LIPI Autonomous/kFoldFolders/D1/'  ## fold0 Train: D0-D1-D2  Test: D1
    #     bwPath = r'C:/Users/fikri/Documents/LIPI Autonomous/result/result2_D1/'
    #     overlayPath = 'C:/Users/fikri/Documents/LIPI Autonomous/overlay/overlay2/'   #fold2

    if kFold == 0:
    ### ================= Fold 2 ================
        rgbPath = r'C:/Users/fikri/Documents/LIPI Autonomous/kFoldFolders/D2/'   ## fold0 Train: D0-D1-D2  Test: D2
        bwPath = r'C:/Users/fikri/Documents/LIPI Autonomous/result/nresult3_D2/'
        overlayPath = 'C:/Users/fikri/Documents/LIPI Autonomous/overlay/overlay3/'   #fold3

    # rgb = cv2.imread(rgbPath)
    # bw = cv2.imread(bwPath)
    NTest = os.listdir(bwPath)

    for item in NTest:
        pathImg = item[:-4]
        rgb = cv2.imread(rgbPath + pathImg + '/images/' + item)
        bw = cv2.imread(bwPath + item)

        M = bw.shape[0]
        N = bw.shape[1]

        seg = np.zeros((M, N, 3), np.uint8)

        for i in range(M):
            for j in range(N):
                if bw[i,j,0] == 255:
                    for k in range(1):
                        rgb[i,j,k] = seg[i,j,k]


        #cv2.imshow("rgb", rgb)
        #cv2.imshow("bw", bw)
        # cv2.imshow("SEG", rgb)
        cv2.imwrite(overlayPath + item, rgb)
        print('success write overlay ' + pathImg)




cv2.waitKey(0)
cv2.destroyAllWindows()