class Solution:
    def evenlist(self, lists):
        new_lists = []
        for item in lists:
            if item % 2 == 0:
                new_lists.append(item)
            else:
                continue
        return new_lists


# 函数算法非常简单，就是遍历列表，提取列表元素中的偶数，然后将其放到一个新的列表中，本次练习主要记录下此函数功能的几种调试方案。
# if __name__ == '__main__':... 是便于调试程序的一种写法，（当程序作为模块使用时，if __name__ == '__main__':内的代码将不执行）

# 方案一：直接输出调试
# 创建一个列表，多次改变列表的内容，观察程序是否正常输出，达到调试的目的。
if __name__ == '__main__':
    solution = Solution()
    lists = [1, 2, 3, 4, 5, 6]
    print(solution.evenlist(lists))

# 方案二：输入输出调试
# 有时候刷题的时候需要写这种输入输出的程序来检验程序的正确性。

# if __name__ == '__main__':
#     solution = Solution()
#     string = input("请输入一个列表:\n例：[1,2,3,4,5]\n请输入：")
#     lists = eval(string)
#     print("从您输入的列表中提取出的偶数组成的新列表如下：")
#     print(solution.evenlist(lists))

# 方案三：面向用户输入调试
# 用户可能不知道[]表示一个列表，所以用户可能会输入一串类似于这样的东东，1,2,3,4,5,6  基于这种输入的调试方案如下。

# if __name__ == '__main__':
#     solution = Solution()
#     string = input("请输入一串数字（用逗号进行分割:\n例：1,2,3,4,5\n请输入：")
#     lists = string.split(',')
#     new_lists = []
#     for item in lists:
#         new_lists.append(int(item))
#     lists = new_lists
#     print("从您输入的列表中提取出的偶数组成的新列表如下：")
#     print(solution.evenlist(lists))

# 一顿操作猛如虎，睡了一觉突然想起来，如果用户不会加一个[]，那我加上去不就行了么，毕竟eval函数如此强大，可以直接将字符串转成正确的列表。
# if __name__ == '__main__':
#     solution = Solution()
#     string = input("请输入一串数字（用逗号进行分割:\n例：1,2,3,4,5\n请输入：")
#     new_string = '[' + string + ']'
#     lists = eval(new_string)
#     print("从您输入的列表中提取出的偶数组成的新列表如下：")
#     print(solution.evenlist(lists))
