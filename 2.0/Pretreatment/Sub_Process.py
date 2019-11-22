from Image_Base import Image_Open, Image_Save_Sub
import os

def Sub_Cut(im, vx, vy, dx, dy):
    """
    切割ROI图片得到原图
    :param im: Image格式图片
    :param vx: 切割的宽
    :param vy: 切割的长
    :param dx: 宽偏移量
    :param dy: 长偏移量
    :return: 子图列表
    """
    sub_Image_List = []
    x1, y1 = 0,0
    x2,y2 = vx, vy
    while x2<= im.size[0]:
        while y2<= im.size[1]:
            sub_im = im.crop((x1, y1, x2, y2))
            sub_Image_List.append(sub_im)

            y1 += dy
            y2 = y1+vy
        x1 += dx
        x2 = x1 + vx
        y1 = 0
        y2 = vy
    return sub_Image_List

def Sub_Save(sub_Image_List,type,fileName):
    """
    将sub_Image_List 中的图片数据保存到本地
    :param sub_Image_List: Image格式图片的列表
    :param type: 类型
    :param fileName:图片名
    :return:
    """
    #确认图片大小，不同尺度保存到不同的文件夹下
    try:
        size = sub_Image_List[0].size[0]
        #改名以及保存子图
        for i in range(len(sub_Image_List)):
            save_Name = fileName.replace('.bmp', '-sub-') + str(i+1)+'.bmp'
            Image_Save_Sub(sub_Image_List[i], size,type,save_Name)
        print(fileName + " 全部子图数量: {}".format(len(sub_Image_List)))
    except:
        print(fileName + " 在这个尺寸下没有子图")

def Sub_Process(type, fileName, vx, vy, dx, dy):
    """
    切割处理
    :param type:图片病灶的类型
    :param fileName: 原图的名字
    :param vx: 切割的宽
    :param vy: 切割的长
    :param dx: 宽偏移量
    :param dy: 长偏移量
    """
    ser_im = Image_Open('./ROI/'+type, fileName)
    sub_Image_List = Sub_Cut(ser_im, vx, vy, dx, dy)
    Sub_Save(sub_Image_List, type, fileName)

# if __name__ == "__main__":
#     pathList = ["ROI/A","ROI/B","ROI/C"]
#     for path in pathList:
#         for _,_,fileNames in os.walk(path):
#             for fileName in fileNames:
#                 if 'ser' in fileName:
#                     Sub_Process(path[-1],fileName,224,224,224,224)
