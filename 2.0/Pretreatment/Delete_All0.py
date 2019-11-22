from PIL import Image
import os
import numpy as np
# path = "subgraph/x32/A/"

#获取sub下所有文件夹位置
pathList = []
#一级目录
path_1 = './subgraph/'
for dir in os.listdir('./subgraph'):
    path_2 = path_1+dir+'/'
    for dir in os.listdir(path_2):
        path_3 = path_2+dir+'/'
        pathList.append(path_3)
# print(pathList)

#删除所有文件夹下图片标准差为0
#防止后面的标准化导致图片分母标准差为0

for path in pathList:
    for _, _, fileNames in os.walk(path):
        for fileName in fileNames:
            try:
                im = Image.open(path + fileName)
                im_array = np.array(im)
                if im_array.std() == 0:
                    os.remove(path + fileName)
                    print("remove: " + fileName)
            except:
                print("删除失败："+fileName)
                continue

