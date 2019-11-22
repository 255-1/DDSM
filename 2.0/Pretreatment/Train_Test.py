import os
import tensorflow as tf
import cv2 as cv
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
from sklearn.model_selection import train_test_split

def Train_Test_Process(size):
    """
    从指定尺寸的文件夹下读取所有图片
    标准化并打上标签
    :param size:子图尺寸
    :return:x_train,x_test,y_train,y_test
    """
    x_data = []
    y_data = []

    A_path = "./subgraph/x"+str(size)+"/A/"
    B_path = "./subgraph/x"+str(size)+"/B/"
    C_path = "./subgraph/x"+str(size)+"/C/"
    path_List = [A_path,B_path,C_path]

    for path in path_List:
        for _,_,fileNames in os.walk(path):
            print(path,'下一共有',len(fileNames),'子图')
            print('开始标准化')
            for fileName in fileNames:
                if 'A' in path:
                    y_data.append([0,0,1])
                if 'B' in path:
                    y_data.append([0,1,0])
                if 'C' in path:
                    y_data.append([1,0,0])
                im = cv.imread(path+fileName)
                im_standard = tf.image.per_image_standardization(im)
                x_data.append(im_standard)
                print('子图标准化处理了',len(x_data))

    return train_test_split(x_data,y_data,test_size=0.33,random_state=42)

# x_train,x_test,y_train,y_test = Train_Test_Process(700)
#
#
# print(x_train)
# print(y_train)
# print(x_test)
# print(y_test)
