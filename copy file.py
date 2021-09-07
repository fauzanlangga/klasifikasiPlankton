import os, shutil

#   directory
rgbPath =  "D:/Magang/Lipi/Train/Jakarta Bay 2019-instance-segmentation/Jakarta Bay 2019/bw/"
rgbFiles = os.listdir(rgbPath)
path =  "D:/Magang/Lipi/Train/Jakarta Bay 2019-instance-segmentation/Jakarta Bay 2019/haha/"

for item in rgbFiles:
    short = item[:-4]
    newPath = path + short
    
    #   copy Path to Folder
    shutil.copy(rgbPath + item,  newPath + "/mask/" + item)

    print("Success Copy File" + newPath + "/" + item)