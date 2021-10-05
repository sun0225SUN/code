# 笔记
```python
# 线性回归最小二乘法


# 引入依赖

import numpy as np
import matplotlib.pyplot as plt

# NumPy 是一个开源的 Python 扩展库，它是 Python 科学计算的基础包。 NumPy 用来支持大数据量的高维数组和矩阵运算。
# Pyplot 是 Matplotlib 的子库，提供了和 MATLAB 类似的绘图 API。

points = np.genfromtxt('data.csv', delimiter=',')
# 导入数据(data.csv)
# 利用np模块的里的gentfromtxt方法读取文件
# 第一个参数指的是文件路径，可以是相对路径或者是绝对路径，也可以是网络路径（下载到当前目录后打开）
# 第二个参数表示以','作为分隔符，（csv格式文件是以“,”分割行数据的一种存储方式）
# numpy.genfromtxt 的具体用法：
# https://www.osgeo.cn/numpy/reference/generated/numpy.genfromtxt.html#numpy.genfromtxt

# 分析points的数据类型
# print(type(points))
# <class 'numpy.ndarray'>
# https://www.runoob.com/numpy/numpy-ndarray-object.html
# 简单来说就是一个（多维）数组

# 提取points中的两列数据，分别为x,y
# 前面是切片，表示提取数据的范围区间，第二个参数表示提取数据的列，索引从0开始
x = points[:, 0]
y = points[:, 1]

# print(type(x))
# <class 'numpy.ndarray'>
# print(type(x[0]))
# <class 'numpy.float64'>
# 发现每列数据都是采用数组的形式存储，单条数据采用浮点型数据存储，不是字符串

# 利用plt画出散点图
plt.scatter(x, y)
plt.show()


# pycharm ctrl+Q 查看函数的参数，这里就是画图，然后展示


# 线性回归; y=wx+b 机器学习求 w 和 b

# 定义损失函数
# 损失函数是稀疏的函数，另外还要传入数据的x,y
def compute_cost(w, b, points):
    total_cost = 0  # 损失误差
    M = len(points)  # 点的个数
    # 逐点计算平方损失误差，然后求平均值
    for i in range(M):
        x = points[i, 0]  # 表示第一列第i个点，即xi
        y = points[i, 1]  # 表示第二列低i个点，即yi
        total_cost += (y - w * x - b) ** 2  # 这里y表示实际值，wx+b表示估计值，单个点误差的平方为(y-(wx+b))²
        return total_cost / M  # 函数返回误差的平方和的平均数（可以理解为方差）


# 定义了一个求取平均数的函数，因为要计算x_bar,y_bar
def average(data):
    sum = 0
    num = len(data)
    for i in range(num):
        sum += data[i]
    return sum / num


# 建模
def fit(points):
    M = len(points)  # 点的个数
    x_bar = average(points[:, 0])  # 第一列所有点的平均值
    y_bar = average(points[:, 0])
    sum_yx = 0
    sum_x2 = 0

    for i in range(M):
        x = points[i, 0]  # 第一列第i个点，即xi
        y = points[i, 1]  # 第二列第i个点，即yi
        sum_yx += y * x
        sum_x2 += x ** 2

    # 根据公式计算W
    fz = sum_yx - M * x_bar * y_bar
    fm = sum_x2 - M * x_bar ** 2
    w = fz / fm

    # 根据公式计算b
    b = y_bar-w*x

    return w, b


# 测试
w, b = fit(points)

print("w is:", w)
print("b is:", b)

cost = compute_cost(w, b, points)
print("cost is:", cost)

# 画出拟合曲线


# 针对每一个x,计算出预测的y值
pred_y = w * x + b
# print(pred_y)
plt.scatter(x, pred_y)
# plt.plot(x, pred_y, c='r')
plt.show()
```
