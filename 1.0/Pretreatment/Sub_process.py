from Image_base import image_open, image_save


def sub_cut(im, filename, vx, vy, dx, dy, cancer):
    """
        切割图片
        :param im: 图片
        :param filename:图片名字（.bmp）
        :param vx: 切割的宽
        :param vy: 切割的长
        :param dx: 切割的宽的偏移量
        :param dy: 切割的长的偏移量
        :return: 切割出来的数量
        """
    try:
        index = 0
        x1, y1 = 0, 0
        x2, y2 = vx, vy
        while x2 <= im.size[0]:
            while y2 <= im.size[1]:
                im2 = im.crop((x1, y1, x2, y2))
                index += 1
                save_name = filename.replace('.bmp', '_sub_')+ str(index) + '.bmp'
                if cancer:
                    image_save(im2, './subgraph/cancer', save_name)
                else:
                    image_save(im2, './subgraph/benign', save_name)
                y1 += dy
                y2 = y1 + vy
            x1 += dx
            x2 = x1 + vx
            y1 = 0
            y2 = vy
    except:
        print('字图切割失败')
    else:
        return index

def Sub_process(path, filename, vx, vy, dx, dy, cancer=True):
    """
    切割简单处理
    :param path: 路径
    :param filename: 图片名字（.bmp）
    :param vx: 切割的宽
    :param vy: 切割的长
    :param dx: 切割的宽的偏移量
    :param dy: 切割的长的偏移量
    """
    im = image_open(path, filename)
    res = sub_cut(im, filename, vx, vy, dx, dy, cancer=cancer)
    print(filename+" total subs:{}".format(res))