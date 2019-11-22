from PIL import Image
import numpy as np
import os
from random import randint

#标准化
def standard_image(im):
    im_array = np.array(im)
    im_array_mean = im_array.mean()
    im_array_std = im_array.std()
    im_array = (im_array - im_array_mean) / im_array_std
    return im_array

def nn_Train_Test_process2(ben_sub_path,can_sub_path,
                          scale, kind):
    """
    生成nn的测试集和训练集
    :param ben_sub_path: 良性子图文件夹
    :param can_sub_path: 恶性子图文件夹
    :param scale: 测试集比训练集的比例
    :param kind: 图片需要的类型
    :return:
    """
    y_train = []
    x_train = []
    y_test = []
    x_test = []
    num_all = 0
    label_dict = {}

    #ben [0,1] can [1,0]
    for filename in os.listdir(ben_sub_path):
        label_dict[filename] = [0, 1]
        num_all += 1
    for filename in os.listdir(can_sub_path):
        label_dict[filename] = [1, 0]
        num_all += 1

    num_rand = num_all / (1 + 1/scale)
    for k, v in label_dict.items():
        if randint(1, num_all) <= num_rand:
            y_test.append(v)
            try:
                im = Image.open(ben_sub_path + '/' + k).convert(kind)
            except:
                im = Image.open(can_sub_path + '/' + k).convert(kind)
            im_array = standard_image(im)
            im_array = np.array(im_array)
            if kind == 'L':
                im_array = im_array.reshape(-1)
            x_test.append(im_array)
        else:
            y_train.append(v)
            try:
                im = Image.open(ben_sub_path + '/' + k).convert(kind)
            except:
                im = Image.open(can_sub_path + '/' + k).convert(kind)
            im_array = standard_image(im)
            im_array = np.array(im_array)
            if kind == 'L':
                im_array = im_array.reshape(-1)
            x_train.append(im_array)

    x_train = np.array(x_train).astype('float32')
    y_train = np.array(y_train).astype('float32')
    x_test = np.array(x_test).astype('float32')
    y_test = np.array(y_test).astype('float32')

    return (x_train, y_train), (x_test, y_test)


def nn_Train_Test_process3(A_sub_path,B_sub_path,C_sub_path,
                          scale, kind):
    """
    生成nn的测试集和训练集
    :param A_sub_path: A
    :param B_sub_path: B
    :param C_sub_path: C
    :param scale: 测试集比训练集的比例
    :param kind: 图片需要的类型
    :return:
    """
    y_train = []
    x_train = []
    y_test = []
    x_test = []
    num_all = 0
    label_dict = {}

    #A [0,0,1] B [0,1,0] C[1,0,0]
    for filename in os.listdir(A_sub_path):
        label_dict[filename] = [0, 0, 1]
        num_all += 1
    for filename in os.listdir(B_sub_path):
        label_dict[filename] = [0, 1, 0]
        num_all += 1
    for filename in os.listdir(C_sub_path):
        label_dict[filename] = [1, 0, 0]
        num_all += 1

    num_rand = num_all / (1 + 1/scale)
    for k, v in label_dict.items():
        if randint(1, num_all) <= num_rand:
            y_test.append(v)
            try:
                im = Image.open(A_sub_path + '/' + k).convert(kind)
            except:
                try:
                    im = Image.open(B_sub_path + '/' + k).convert(kind)
                except:
                    im = Image.open(C_sub_path + '/' + k).convert(kind)
            im_array = standard_image(im)
            im_array = np.array(im_array)
            if kind == 'L':
                im_array = im_array.reshape(-1)
            x_test.append(im_array)
        else:
            y_train.append(v)
            try:
                im = Image.open(A_sub_path + '/' + k).convert(kind)
            except:
                try:
                    im = Image.open(B_sub_path + '/' + k).convert(kind)
                except:
                    im = Image.open(C_sub_path + '/' + k).convert(kind)
            im_array = standard_image(im)
            im_array = np.array(im_array)
            if kind == 'L':
                im_array = im_array.reshape(-1)
            x_train.append(im_array)

    x_train = np.array(x_train).astype('float32')
    y_train = np.array(y_train).astype('float32')
    x_test = np.array(x_test).astype('float32')
    y_test = np.array(y_test).astype('float32')

    return (x_train, y_train), (x_test, y_test)

def nn_Train_Test_process4(Nothing_sub_path, A_sub_path,B_sub_path,C_sub_path,
                          scale, kind):
    """
    生成nn的测试集和训练集
    :param Nothing_sub_path: 没事的
    :param A_sub_path: A
    :param B_sub_path: B
    :param C_sub_path: C
    :param scale: 测试集比训练集的比例
    :param kind: 图片需要的类型
    :return:
    """
    y_train = []
    x_train = []
    y_test = []
    x_test = []
    num_all = 0
    label_dict = {}

    #Nothing [0,0,0,1] A [0,0,1,0] B[0,1,0,0] C[1,0,0,0]
    for filename in os.listdir(Nothing_sub_path):
        label_dict[filename] = [0, 0, 0, 1]
        num_all += 1
    for filename in os.listdir(A_sub_path):
        label_dict[filename] = [0, 0, 1, 0]
        num_all += 1
    for filename in os.listdir(B_sub_path):
        label_dict[filename] = [0, 1, 0, 0]
        num_all += 1
    for filename in os.listdir(C_sub_path):
        label_dict[filename] = [1, 0, 0, 0]
        num_all += 1


    num_rand = num_all / (1 + 1/scale)
    for k, v in label_dict.items():
        if randint(1, num_all) <= num_rand:
            y_test.append(v)
            try:
                im = Image.open(A_sub_path + '/' + k).convert(kind)
            except:
                try:
                    im = Image.open(B_sub_path + '/' + k).convert(kind)
                except:
                    try:
                        im = Image.open(C_sub_path + '/' + k).convert(kind)
                    except:
                        im = Image.open(Nothing_sub_path + '/' + k).convert(kind)
            im_array = standard_image(im)
            im_array = np.array(im_array)
            if kind == 'L':
                im_array = im_array.reshape(-1)
            x_test.append(im_array)
        else:
            y_train.append(v)
            try:
                im = Image.open(A_sub_path + '/' + k).convert(kind)
            except:
                try:
                    im = Image.open(B_sub_path + '/' + k).convert(kind)
                except:
                    try:
                        im = Image.open(C_sub_path + '/' + k).convert(kind)
                    except:
                        im = Image.open(Nothing_sub_path + '/' + k).convert(kind)
            im_array = standard_image(im)
            im_array = np.array(im_array)
            if kind == 'L':
                im_array = im_array.reshape(-1)
            x_train.append(im_array)

    x_train = np.array(x_train).astype('float32')
    y_train = np.array(y_train).astype('float32')
    x_test = np.array(x_test).astype('float32')
    y_test = np.array(y_test).astype('float32')

    return (x_train, y_train), (x_test, y_test)