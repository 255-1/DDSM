from ROI_and_Sub_process import ROI_and_Sub_process
from Train_Test_process import *

def pic_process(d, v):
    """
    图片批处理
    :param d: 子图长宽
    :param v: 子图偏移量
    """
    path_ben = input('良性原图和截图共同的位置：')
    path_can = input('恶性原图和截图共同的位置：')
    ROI_and_Sub_process(path_ben, d, v, cancer=False)
    ROI_and_Sub_process(path_can, d, v, cancer=True)

def label2_for_nn(ben_path,
                 can_path,
                 scale , kind='L'):
    (x_train, y_train), (x_test, y_test) = nn_Train_Test_process2(ben_sub_path=ben_path,
                                                                 can_sub_path=can_path,
                                                                 scale=scale, kind=kind)
    return (x_train, y_train), (x_test, y_test)

def label3_for_nn(A_path, B_path, C_path, scale , kind='L'):
    (x_train, y_train), (x_test, y_test) = nn_Train_Test_process3(A_sub_path=A_path,
                                                                 B_sub_path=B_path,
                                                                 C_sub_path=C_path,
                                                                 scale=scale, kind=kind)
    return (x_train, y_train), (x_test, y_test)

def label4_for_nn(Nothing_path, A_path, B_path, C_path, scale, kind='L'):
    (x_train, y_train), (x_test, y_test) = nn_Train_Test_process4(Nothing_sub_path=Nothing_path,
                                                                 A_sub_path=A_path,
                                                                 B_sub_path=B_path,
                                                                 C_sub_path=C_path,
                                                                 scale=scale, kind=kind)
    return (x_train, y_train), (x_test, y_test)