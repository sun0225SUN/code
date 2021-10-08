# 引入依赖
import numpy as np
import matplotlib.pyplot as plt


class Solution:
    # 定义损失函数
    def compute_cost(self, w, b, points):
        total_cost = 0  # 损失误差
        M = len(points)  # 点的个数
        # 逐点计算平方损失误差，然后求平均值
        for i in range(M):
            x = points[i, 0]  # 表示第一列第i个点，即xi
            y = points[i, 1]  # 表示第二列低i个点，即yi
            total_cost += (y - w * x - b) ** 2  # 这里y表示实际值，wx+b表示估计值，单个点误差的平方为(y-(wx+b))²，+=计算累加值

        return total_cost / M  # 函数返回误差的平方和的平均数（本例的损失函数可以理解为计算方差）

    # 定义了一个求取平均数的函数，因为要计算x_bar，y_bar
    def average(self, data):
        sum = 0
        num = len(data)
        for i in range(num):
            sum += data[i]
        return sum / num

    # 拟合函数
    def fit(self, points):
        M = len(points)  # 点的个数
        x_bar = self.average(points[:, 0])  # 第一列所有点的平均值
        y_bar = self.average(points[:, 1])  # 第二列所有点的平均值
        sum_yx = 0  # 计算分子累加和部分
        sum_x2 = 0  # 计算分母累加和部分,累加要有初始值，初始化为0

        for i in range(M):
            x = points[i, 0]  # 第一列第i个点，即xi
            y = points[i, 1]  # 第二列第i个点，即yi
            sum_yx += y * x  # 分子累加部分
            sum_x2 += x ** 2  # 分母累加部分

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

    # 针对每一个x,计算出预测的y值
    pred_y = w * x + b
    # 画出拟合曲线
    plt.scatter(x, pred_y)
    plt.show()
