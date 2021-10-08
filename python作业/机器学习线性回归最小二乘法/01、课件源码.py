# 线性回归最小二乘法

# 引入依赖
import numpy as np
import matplotlib.pyplot as plt

points = np.genfromtxt('data.csv', delimiter=',')

x = points[:, 0]
y = points[:, 1]

# 利用plt画出散点图
plt.scatter(x, y)
plt.show()


# 定义损失函数
# 损失函数是稀疏的函数，另外还要传入数据的x,y
def compute_cost(w, b, points):
    total_cost = 0
    M = len(points)
    # 逐点计算平方损失误差，然后求平均值
    for i in range(M):
        x = points[i, 0]
        y = points[i, 1]
        total_cost += (y - w * x - b) ** 2
    return total_cost / M


# 定义了一个求取平均数的函数，因为要计算x_bar,y_bar
def average(data):
    sum = 0
    num = len(data)
    for i in range(num):
        sum += data[i]
    return sum / num


# 拟合函数
def fit(points):
    M = len(points)  #
    x_bar = average(points[:, 0])
    sum_yx = 0
    sum_x2 = 0
    sum_delta = 0

    for i in range(M):
        x = points[i, 0]
        y = points[i, 1]
        sum_yx += y * (x - x_bar)
        sum_x2 += x ** 2
    w = sum_yx / (sum_x2 - M * (x_bar ** 2))

    for i in range(M):
        x = points[i, 0]
        y = points[i, 1]
        sum_delta += (y - w * x)
    b = sum_delta / M

    return w, b


# 测试
w, b = fit(points)

print("w is:", w)
print("b is:", b)

cost = compute_cost(w, b, points)
print("cost is:", cost)

# 画出拟合曲线
pred_y = w * x + b  # 针对每一个x,计算出预测的y值
plt.scatter(x, pred_y)
plt.show()
