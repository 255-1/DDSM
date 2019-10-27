import skimage
from skimage import io
from PIL import Image
import numpy as np
from skimage.measure import compare_psnr
import matplotlib.pyplot as plt
P = 0
P1 = 0
P2 = 0
result_1 = []
result_2 = []
for j in range(1 , 6):
    for i in range(1,135):
        path = 'D:/SVM/benign/' + str(i) + '.bmp'
        img = io.imread(path)
        img1 = skimage.util.random_noise(img, mode='gaussian', seed=None, clip=True, mean = j * 0.000001,
                                         var = j * 0.000001)
        path_Noise = 'D:/SVM/benign(Noise)/' + str(i) + '.bmp'
        io.imsave(path_Noise, img1)

        im1 = np.array(Image.open(path), 'f')
        im2 = np.array(Image.open(path_Noise), 'f')
        p1 = compare_psnr(im1, im2, 255)
        P1 = P1 + p1
    P1 = P1 / 135

    for i in range(1, 158):
        path = 'D:/SVM/cancer/' + str(i) + '.bmp'
        img = io.imread(path)
        img1 = skimage.util.random_noise(img, mode='gaussian', seed=None, clip=True, mean=0.1,
                                         var=0.1)
        path_Noise = 'D:/SVM/cancer(Noise)/' + str(i) + '.bmp'
        io.imsave(path_Noise, img1)

        im1 = np.array(Image.open(path), 'f')
        im2 = np.array(Image.open(path_Noise), 'f')
        p1 = compare_psnr(im1, im2, 255)
        P2 = P2 + p1
    P2 = P2 / 158

    P = P1 + P2
    result_1 = result_1 + [P/2]
    print("信噪比：%f" % (P/2))
    # 提取特征（）
    #   return 表格的地址

    # result = 机器学习（表格地址）
    # result_2 = result_2 + [result]
print(result_1)
print(result_2)

# plt.figure()
# plt.plot(result_1,result_2)
# plt.xlabel("PSNR")
# plt.ylabel("")
# plt.show()


