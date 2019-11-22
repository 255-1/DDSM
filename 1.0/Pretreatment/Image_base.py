import os
from PIL import Image

#打开图片
def image_open(path, filename):
    try:
        Image.open(path+'/'+filename)
    except:
        print("打开图片失败")
    else:
        return Image.open(path+'/'+filename)

#保存图片
def image_save(im, path, filename):
    try:
        if not os.path.exists(path):
            os.makedirs(path)
        filename = filename[:-4:] + '.bmp'
        im.save(path + '/' + filename)
    except:
        print('图片保存失败')
