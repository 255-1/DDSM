from PIL import Image
import os
from Image_base import image_save

def pixel_wanted(pix):
    return pix==(237,28, 36)

def fillPoly(im):
    coordinate_List = []

    top_Pixel = (0,0,0)
    for x in range(im.size[0]):
        flag = False #初始化每一列翻转位为False
        for y in range(im.size[1]):
            current_pixel = im.getpixel((x,y))
            last_pixel = im.getpixel((x,y-1)) if y>0 else top_Pixel
            #翻转判定
            if pixel_wanted(current_pixel) and \
                    not pixel_wanted(last_pixel):
                flag = True
            if flag and not pixel_wanted(current_pixel):
                flag = False
            if(flag):
                coordinate_List.append((x,y))
    coordinate_Min_Max_List = []
    #找最小最大
    for i in range(im.size[0]):
        min=-1
        max=-1
        for coordinate in coordinate_List:
            if coordinate[0] == i:
                min = coordinate[1]
                max = coordinate[1]
                break
        for coordinate in coordinate_List:
            if coordinate[0] == i:
                if coordinate[1]>max:
                    max = coordinate[1]
        coordinate_Min_Max_List.append(min)
        coordinate_Min_Max_List.append(max)
    #上色
    for x in range(im.size[0]):
        for y in range(im.size[1]):
            min = coordinate_Min_Max_List[x*2]
            max = coordinate_Min_Max_List[x*2+1]
            if min<y<max:
                im.putpixel((x,y),(0,255,0))
            else:
                #可以把非红圈的上掩膜遮住
                pass
    return im

def Cal_S(im):
    im_0 = im.rotate(0)
    im_90 = im.rotate(90, expand=True)

    im_0 = fillPoly(im_0)
    im_90 = fillPoly(im_90)
    im_90 = im_90.rotate(-90, expand=True)

    i=0
    for x in range(im.size[0]):
        for y in range(im.size[1]):
            if(im_0.getpixel((x,y))==(0,255,0) and
            im_90.getpixel((x,y))==(0,255,0)):
                im.putpixel((x,y),(0,255,0))
                i+=1
    return i/(im.size[0]*im.size[1])

if __name__ =="__main__":
    pathList = ["ROI/A/", "ROI/B/", "ROI/C/"]
    for path in pathList:
        for _,_,fileNames in os.walk(path):
            for fileName in fileNames:
                if 'roi' in fileName:
                    im = Image.open(path+fileName)
                    # image_save(im,'ROI_Cal/'+path[4]+'/',fileName)
    #                 print('开始处理',fileName,'面积大小')
                    print(Cal_S(im))
    #
    #                 # image_save(im, 'ROI_Cal/'+path[4]+'/',fileName.replace('.bmp','-%.2f.bmp'%area))
    # print(max(area_list))