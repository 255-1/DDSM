from Image_base import image_open, image_save
#判断像素点是否在范围
def pixel_wanted(pix):
    return pix>(255, 0, 0) and pix<(255, 30, 30)

#获取截图ROI位置
def gain_position(im):
    """
        获取ROI坐标
        :param im: 图片
        :return: 左上右下四个点像素位置
    """
    x_list = []
    y_list = []

    try:
        for x in range(im.size[0]):
            for y in range(im.size[1]):
                if pixel_wanted(im.getpixel((x, y))):
                    x_list.append(x)
                    y_list.append(y)
    except :
        print('截图ROI获取失败')
    else:
        return min(x_list), min(y_list), max(x_list), max(y_list)

#计算两张图比例
def cal_scale(im1, im2):
    try:
        judge = im1.size[0]>im2.size[0] and im1.size[1]>im2.size[1]
        if judge:
            scale = (im1.size[0] / im2.size[0] + im1.size[1] / im2.size[1]) / 2
        else:
            scale = (im2.size[0] / im1.size[0] + im2.size[1] / im1.size[1]) / 2
    except:
        print('计算图片比例失败')
    else:
        return scale

#截取ROI
def ROI_cut(im, x_min, y_min, x_max, y_max):
    try:
        im = im.crop((x_min, y_min, x_max, y_max))
    except:
        print('至少三点共线')
    else:
        return im

def ROI_process(path, filename, cancer = True):
    """
    :param path:
    :param filename: bmp后缀
    :return:
    """
    ori_im = image_open(path, filename)
    refer_im = image_open(path, filename.replace('bmp', 'png'))

    scale = cal_scale(ori_im, refer_im)
    left, up, right, down = gain_position(refer_im)
    ori_left, ori_up, ori_right, ori_down = left * scale, up * scale, right * scale, down * scale
    ROI_im = ROI_cut(ori_im, ori_left, ori_up, ori_right, ori_down)
    if cancer:
        image_save(ROI_im, './ROI/cancer', filename)
    else:
        image_save(ROI_im, './ROI/benign', filename)
    print(filename+' ROI_size:'+repr(ROI_im.size))
