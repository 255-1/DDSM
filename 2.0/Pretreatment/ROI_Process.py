from Image_Base import Image_Save_ROI,Image_Open

def Pixel_Wanted(pixel):
    """
    判断像素点是否符合期望像素RGB值
    :param pixel: 像素点
    :return: 是否符合期望像素的RGB
    """
    return pixel==(237, 28, 36)


def Gain_Position(im):
    """
    获取病灶ROI的大小
    :param im:Image格式图片
    :return:符合Image.crop参数的左上和右下坐标
    """
    x_list = []
    y_list = []

    for x in range(im.size[0]):
        for y in range(im.size[1]):
            if Pixel_Wanted(im.getpixel((x,y))):
                x_list.append(x)
                y_list.append(y)
    return min(x_list),min(y_list),max(x_list),max(y_list)

def Cal_Scale(im1, im2):
    """
    计算两张图片的比例大小
    :param im1:
    :param im2:
    :return:
    """
    scale = (im1.size[0]/im2.size[0]+im1.size[1]/im2.size[1])/2
    return scale if scale>1 else 1/scale

def ROI_Process(type, fileName):
    """
    ROI处理
    :param type: 图片病灶的类型
    :param fileName: 原图的名字
    :return:
    """
    ser_im = Image_Open('./Data/'+type, fileName)
    roi_im = Image_Open('./Data/'+type, fileName.replace('ser','roi'))

    scale = Cal_Scale(ser_im, roi_im)
    roi_left,roi_up,roi_right,roi_down = Gain_Position(roi_im)
    ser_left,ser_up,ser_right,ser_down = \
        roi_left * scale, roi_up * scale, roi_right * scale, roi_down * scale

    ser_im = ser_im.crop((ser_left,ser_up,ser_right,ser_down))
    Image_Save_ROI(ser_im,type,fileName)

    print(fileName+' ROI size is :'+repr(ser_im.size))
