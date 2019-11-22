from ROI_process import ROI_process
from Sub_process import Sub_process
import os

# path_ben = '/home/zhi-jun/MHD/DDSM/4_benign_Pleo_10'
# path_can = '/home/zhi-jun/MHD/DDSM/4_cancer_Pleo_10'

def ROI_and_Sub_process(path, d, v, cancer):
    """
    :param path: 原图和截图所在文件夹
    :param cancer:bool值,是否是恶性的图
    :param d:子图长宽
    :param v: 剪切偏移量
    :return:
    """
    for filename in os.listdir(path):
        if 'bmp' in filename:
            ROI_process(path, filename,cancer)

    if cancer:
        print('cancer ROI Success')
        ROI_path = './ROI/cancer'
    else:
        print('benign ROI Success')
        ROI_path = './ROI/benign'

    for filename in os.listdir(ROI_path):
        Sub_process(ROI_path, filename,
                    d, d, v, v,cancer)
    if cancer:
        print('cancer Sub Success')
    else:
        print('benign Sub Success')



