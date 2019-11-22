from ROI_Process import ROI_Process
from Sub_Process import Sub_Process
import os

"""
图片预处理得到ROI和sub的操作
"""

vx=700
vy=700
dx=700
dy=700

# A_data_path = './Data/A/'
# B_data_path = './Data/B/'
# C_data_path = './Data/C/'
# pathList = [A_data_path,B_data_path,C_data_path]
#
# for path in pathList:
#     for _,_,fileNames in os.walk(path):
#         for fileName in fileNames:
#             ROI_Process(path[-2],fileName)

A_ROI_path = './ROI/A/'
B_ROI_path = './ROI/B/'
C_ROI_path = './ROI/C/'

pathList = [A_ROI_path,B_ROI_path,C_ROI_path]

for path in pathList:
    for _, _, fileNames in os.walk(path):
        for fileName in fileNames:
            if 'ser' in fileName:
                Sub_Process(path[-2],fileName,vx,vx,dx,dx)