# 引入依赖
import numpy as np
import matplotlib.pyplot as plt


class Solution:
    # 定义损失函数
    def compute_cost(self, w, b, points):
        total_cost = 0
        M = len(points)
        for i in range(M):
            x = points[i, 0]
            y = points[i, 1]
            total_cost += (y - w * x - b) ** 2
        return total_cost / M 

    # 定义了一个求取平均数的函数，因为要计算x_bar，y_bar
    def average(self, data):
        sum = 0
        num = len(data)
        for i in range(num):
            sum += data[i]
        return sum / num

    # 拟合函数
    def fit(self, points):
        M = len(points)
        x_bar = self.average(points[:, 0])
        y_bar = self.average(points[:, 1])
        sum_yx = 0
        sum_x2 = 0

        for i in range(M):
            x = points[i, 0]
            y = points[i, 1]
            sum_yx += y * x
            sum_x2 += x ** 2

        # 根据公式计算W
        fz = sum_yx - M * x_bar * y_bar
        fm = sum_x2 - M * x_bar ** 2
        w = fz / fm

        # 根据公式计算b
        b = y_bar - w * x_bar

        return w, b


# 测试
if __name__ == '__main__':
    # 创建一个解决方案对象
    solution = Solution()
    # 导入数据
    points = np.genfromtxt('data.csv', delimiter=',')
    # 提取两列数据
    x = points[:, 0]
    y = points[:, 1]
    # 利用plt画出散点图
    plt.scatter(x, y)
    plt.show()

    # 求得x和y所建立的线性回归方程中的参数w和b
    w, b = solution.fit(points)
    # 打印出参数的值
    print("w is:", w)
    print("b is:", b)
    # 求得损失函数误差值
    cost = solution.compute_cost(w, b, points)
    # 打印
    print("cost is:", cost)

    # 展示拟合曲线
    # 画出散点图
    plt.scatter(x, y)
    # 针对每一个x,计算出预测的y值
    pred_y = w * x + b
    # 画出拟合线
    plt.plot(x, pred_y, c='r')
    # 展示
    plt.show()
