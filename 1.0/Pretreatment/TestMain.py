from Preprocess import *

A_path = 'G:/DDSM/benign_M&R'
B_path = 'G:/DDSM/cancer_M&R'
C_path = 'G:/DDSM/C'
Nothing_path = 'G:/DDSM/Nothing'


(x_train, y_train), (x_test, y_test) = label2_for_nn(A_path, B_path, 1/4, kind='RGB')
print(x_train.shape)
print(y_train.shape)
print(x_test.shape)
print(y_test.shape)

# (x_train, y_train), (x_test, y_test) = label3_for_nn(A_path, B_path, C_path, 1/4, kind='RGB')
# print(x_train.shape)
# print(y_train.shape)
# print(x_test.shape)
# print(y_test.shape)
#
#
# (x_train, y_train), (x_test, y_test) = label4_for_nn(Nothing_path, A_path, B_path, C_path, 1/4, kind='RGB')
# print(x_train.shape)
# print(y_train.shape)
# print(x_test.shape)
# print(y_test.shape)