from sklearn import svm,metrics
import numpy as np
from sklearn.model_selection import train_test_split, learning_curve
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.utils import shuffle

data = pd.read_excel('D:\SVM\\test_all.xlsx')
pre_data = data.iloc[0:, 1:]
X = pre_data.iloc[:, :53]
y = pre_data.iloc[:, 53]
x_train, x_test, y_train, y_test = train_test_split(X, y, random_state=1, train_size=0.75)

clf_rbf = svm.SVC(kernel='rbf')
clf_rbf.fit(x_train, y_train.ravel())
print('rbf_train:%.2f' % clf_rbf.score(x_train, y_train))
print('rbf_test:%.2f' % clf_rbf.score(x_test, y_test))

#绘制学习曲线
X_shuffle, y_shuffle = shuffle(X, y)
plt.figure(figsize=(7, 5))
train_sizes, train_scores, test_scores = learning_curve(clf_rbf,X_shuffle,y_shuffle)
train_scores_mean = np.mean(train_scores, axis=1)
test_scores_mean = np.mean(test_scores, axis=1)
plt.plot(train_sizes, train_scores_mean, 'o-', color='red', label='Train_Score = %0.2f' % clf_rbf.score(x_train, y_train) )
plt.plot(train_sizes, test_scores_mean, 'o-', color='blue', label='Test_Score = %0.2f' % clf_rbf.score(x_test, y_test))
plt.xlim([0.0, 200.0])
plt.ylim([0.5, 1.2])
plt.legend(loc="lower right")
plt.title("Learning Curve")


#绘制ROC
metrics.f1_score(y_test,clf_rbf.predict(x_test))
fpr,tpr,thresholds=metrics.roc_curve(y_test,clf_rbf.decision_function(x_test),
pos_label=2)
roc_auc = metrics.auc(fpr,tpr)
plt.figure(figsize=(8, 5))
plt.plot(fpr, tpr, color='darkorange',lw=2, label='ROC curve (area = %0.2f)' % roc_auc)  # 假正率为横坐标，真正率为纵坐标做曲线
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.title("ROC")
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.legend(loc="lower right")
plt.show()


# clf_sigmoid = svm.SVC(kernel='sigmoid')
# clf_sigmoid.fit(x_train, y_train.ravel())
# print('sigmoid_train:%.2f' % clf_sigmoid.score(x_train, y_train))
# print('sigmoid_test:%.2f' % clf_sigmoid.score(x_test, y_test))
#
# clf_poly = svm.SVC(kernel='poly')
# clf_poly.fit(x_train, y_train.ravel())
# print('poly_train%.2f:' % clf_poly.score(x_train, y_train))
# print('poly_test%.2f:' % clf_poly.score(x_test, y_test))


# X_shuffle, y_shuffle = shuffle(X, y)
# plot_learning_curve(clf_rbf,X_shuffle,y_shuffle)
# plt.show()
# plot_learning_curve(clf_sigmoid,X_shuffle,y_shuffle)
# plt.show()
# plot_learning_curve(clf_poly,X_shuffle,y_shuffle)
# plt.show()