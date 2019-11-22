import os
from PIL import Image

#打开图片
def Image_Open(path, fileName):
    """
    打开图片工具，
    :param path:打开路径，以'/'结尾
    :param fileName: 打开的文件名
    :return: Image格式的图片
    """
    try:
        Image.open(path+'/'+fileName)
    except:
        print("图片:"+fileName+"打开失败")
    else:
        return Image.open(path+'/'+fileName)


def Image_Save(im, path, fileName):
    """
    保存图片工具
    :param im:Image格式的图片
    :param path: 保存路径，以'/'结尾
    :param fileName: 保存的文件名
    :return: 无
    """
    try:
        if not os.path.exists(path):
            os.makedirs(path)
        im.save(path + '/' + fileName)
    except:
        print('图片:'+fileName+'保存失败')

def Image_Save_Sub(im, size, type, fileName):
    """
    子图保存
    :param im:Image格式图片
    :param size: 子图切割大小
    :param type: 病灶种类
    :param fileName: 保存文件名
    :return:
    """
    try:
        save_path = './subgraph/x'+str(size)+'/'+type
        Image_Save(im, save_path, fileName)
    except:
        print('子图:'+fileName+'保存失败')

def Image_Save_ROI(im, type, fileName):
    """
    ROI图片保存
    :param im:Image格式图片
    :param type: ROI病灶种类
    :param fileName: 保存的文件名
    :return:
    """
    try:
        save_path = './ROI/' + type
        Image_Save(im, save_path, fileName)
    except:
        print('ROI: '+fileName+'保存失败')

# def Image_Save_StandardSub(im, size, type, fileName):
#     """
#     标准化子图图片保存
#     :param im: Image格式图片
#     :param type: 病灶类型
#     :param fileName: 保存的文件名
#     :return:
#     """
#     try:
#         save_path='./subgraph/x'+str(size)+'-standard/'+type
#         Image_Save(im, save_path, fileName)
#     except:
#         print('标准化子图:' + fileName + '保存失败')