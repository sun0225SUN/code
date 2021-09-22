# 新建一个列表，存储学生信息，学生的信息采用字典的方式存储，0表示女性，1表示男性
info = [{'name': '小千', 'sex': '0', 'score': '95'},
        {'name': '小锋', 'sex': '1', 'score': '99'},
        {'name': '小扣', 'sex': '0', 'score': '86'},
        {'name': '小丁', 'sex': '1', 'score': '88'},
        {'name': '小明', 'sex': '1', 'score': '90'}]
# filter() 函数用于过滤序列，过滤掉不符合条件的元素，（返回由符合条件元素组成的新列表）python3中返回的是一个fileter对象，所以需要转换成列表。
# 语法为  filter(function, iterable) 参数分别为一个函数和一个可迭代的对象，本处表示过滤掉女性童鞋。
temp1 = list(filter(lambda x: x['sex'] == '1', info))
# sorted函数是python中的内置函数，用于对所有可迭代对象进行排序操作。
# 语法为sorted(iterable, cmp=None, key=None, reverse=False)。
# 第一个参数是一个可迭代对象，cmp和key为比较函数，cmp可以拥有两个参数，key只允许一个参数，默认由低到高排序，reverse设置为ture为逆序。
temp2 = sorted(temp1, key=lambda x: x['score'], reverse=True)
# 过滤女同学后，并且对男同学的信息以成绩为标准从高到低排序后，现在需要做的是打印出男同学的名字和成绩。
# 遍历temp2列表，每一次循环，x表示一名男同学的信息，以字典的形式存储。
for x in temp2:
    # 遍历字典中的键和值
    for key, value in x.items():
        # 如果键不为'sex'，则输出与键对应的值。
        if key != 'sex':
            # print()函数的第三个参数'end'默认为'\n',本处表示：打印一行文字后不换行，而是输出一个空格。
            print(value, end=' ')
    # 遍历完一名学生，也就是输出完一名学生的信息后，利用print()进行换行。
    print()
    # 继续循环，遍历下一名学生⬆️


# 吐槽一下，PPT里的程序是有问题的，虽然问题很小，但是debug还是浪费了一点时间。
# 问题就在于过滤列表中的过滤函数判断项，应该是x['sex']=='1',而不是x['sex']==1，要不然所有的数据都过滤掉了。


# 将lambda函数改成标准函数。

# def del_girl(x):
#     return x['sex'] == '1'
#
#
# def sort_score(x):
#     return x['score']
#
#
# info = [{'name': '小千', 'sex': '0', 'score': '95'},
#         {'name': '小锋', 'sex': '1', 'score': '99'},
#         {'name': '小扣', 'sex': '0', 'score': '86'},
#         {'name': '小丁', 'sex': '1', 'score': '88'},
#         {'name': '小明', 'sex': '1', 'score': '90'}]
# temp1 = list(filter(del_girl, info))
# temp2 = sorted(temp1, key=sort_score, reverse=True)
# for x in temp2:
#     for key, value in x.items():
#         if key != 'sex':
#             print(value, end=' ')
#     print()
