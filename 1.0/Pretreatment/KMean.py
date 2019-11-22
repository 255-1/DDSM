import xlrd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.feature_selection import f_regression
from scipy.stats import kstest
from scipy.stats import levene
from scipy.stats import f_oneway
from scipy.stats import chisquare
from scipy.stats import fisher_exact
from f_score import fisher_score

def read_Excel(filename):
    """
    读取excel数据，返回只带特征的dataframe矩阵

    :param filename: excel特征文件路径
    :return: pd.DataFrame类型
    """
    wb = xlrd.open_workbook(filename=filename)
    table = wb.sheet_by_index(0)
    a = []
    for i in range(1, table.nrows):
        row_data = table.row_values(i)[1:-1]
        a.append(row_data)
    return pd.DataFrame(a)

#验证所有数据是否符合正态分布
def isNorm(data):
    for i in range(data.shape[1]):
        col = data[i]
        static,p_value = kstest(col,'norm')
        if(p_value<0.03):
            continue
        else:
            print('第{}列数据不符合正态分布'.format(i))
            return 0;
#检验相邻数据的方差齐性
def isHomo(data):
    print("levene检查方差齐性")
    for i in range(data.shape[1] - 1):
        flag = False
        p_value = levene(data[i], data[i + 1])[1]
        if (p_value < 0.05):
            flag = True
        if (flag == False):
            print("{}和{}列不符合方差齐性".format(i + 1, i + 2))
    print("f检验方差齐性")
    for i in range(data.shape[1] - 1):
        flag = False
        p_value = f_oneway(data[i], data[i + 1])[1]
        if (p_value < 0.05):
            flag = True
        if (flag == False):
            print("{}和{}列不符合方差齐性".format(i + 1, i + 2))

    # print("卡方检验方差齐性")
    # for i in range(data.shape[1]-1):
    #     flag = False
    #     p_value = chisquare(data[:,i],data[:,i+1])[1]
    #     if(p_value<0.05):
    #         flag = True
    #     if(flag == False):
    #         print("{}和{}列不符合方差齐性".format(i+1,i+2))


    # 有异常列需要调整

#零-均值归一化
def std_data(data):
    return (data-data.mean())/data.std()


def plot_basic_scatter(data,feature1,feature2):
    """
    取两个特征，绘制未聚类的散点图
    :param feature1:第feature1个特征
    :param feature2: 第feature2个特征
    :return:
    """
    plt.figure()
    plt.scatter(data[feature1],data[feature2],color='blue')
    plt.xlabel('特征{}'.format(feature1))
    plt.ylabel('特征{}'.format(feature2))
    plt.show()
    # 有异常点需要清理

def clf_add_label(data, n):
    """
    聚类加上标签
    :param data:
    :param n:
    :return:
    """
    clf = KMeans(n_clusters=n)
    clf = clf.fit(data)
    data['label'] = clf.labels_
    return data

def plot_2label_scatter(data,feature1,feature2):
    data0 = data.loc[data['label'] == 0]
    data1 = data.loc[data['label'] == 1]
    plt.figure()
    plt.scatter(data0[feature1], data0[feature2], color='yellow')
    plt.scatter(data1[feature1], data1[feature2], color='blue')
    plt.xlabel('特征{}'.format(feature1))
    plt.ylabel('特征{}'.format(feature2))
    plt.show()

def plot_3label_scatter(data,feature1,feature2):
    data0 = data.loc[data['label'] == 0]
    data1 = data.loc[data['label'] == 1]
    data2 = data.loc[data['label'] == 2]
    plt.figure()
    plt.scatter(data0[feature1], data0[feature2], color='yellow')
    plt.scatter(data1[feature1], data1[feature2], color='blue')
    plt.scatter(data2[feature1], data2[feature2], color='green')
    plt.xlabel('特征{}'.format(feature1))
    plt.ylabel('特征{}'.format(feature2))
    plt.show()

def plot_4label_scatter(data,feature1,feature2):
    data0 = data.loc[data['label'] == 0]
    data1 = data.loc[data['label'] == 1]
    data2 = data.loc[data['label'] == 2]
    data3 = data.loc[data['label'] == 3]
    plt.figure()
    plt.scatter(data0[feature1], data0[feature2], color='yellow')
    plt.scatter(data1[feature1], data1[feature2], color='red')
    plt.scatter(data2[feature1], data2[feature2], color='green')
    plt.scatter(data3[feature1], data3[feature2], color='blue')
    plt.xlabel('特征{}'.format(feature1))
    plt.ylabel('特征{}'.format(feature2))
    plt.show()

if __name__ == '__main__':
    filename = './data/模拟数据.xls'
    #读取数据，判断各个特征是否符合正态分布和方差齐性
    data = read_Excel(filename)
    isNorm(data)
    isHomo(data)
    #零-均值归一化
    data = std_data(data)
    #绘制基本散点图
    # for i in range(data.shape[1]-1):
    #     plot_basic_scatter(data,i,i+1)

    #聚类加标签
    data = clf_add_label(data,53)

    # 绘制聚类玩的散点图
    # for i in range(data.shape[1]-1):
    #     plot_4label_scatter(data,i,i+1)

    # #计算f_score
    feature_matrix = data[range(data.shape[1]-1)]
    label_matrix = data['label']
    f_score,p_value = f_regression(feature_matrix,label_matrix)
    len = len(f_score)

    f_score_1 = sorted(f_score)[:len//3]
    f_score_2 = sorted(f_score)[len//3:2*len//3]
    f_score_3 = sorted(f_score)[2*len//3:len]

    print(np.average(f_score_1))
    print(np.average(f_score_2))
    print(np.average(f_score_3))

    for i in range(len(p_value)):
        if(p_value[i]<0.05):
            continue
        else:
            f_score[i] = 0
    print(np.argsort(f_score))

    # feature_matrix = np.array(feature_matrix)
    # fi_score = fisher_score(feature_matrix,label_matrix)
    # print(fi_score)


