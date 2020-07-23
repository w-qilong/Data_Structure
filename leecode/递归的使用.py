# -*- encoding: utf-8 -*-
"""
@File    : 递归的使用.py
@Time    : 2020/5/5 9:14
@Author  : WuQilong
@Email   : 1528625919@qq.com
@Software: PyCharm
"""


# 通常情况下，涉及到数组的递归函数时，基线条件通常是数组为空或只包含一个元素。
# 递归使用的步骤：1.寻找基线条件，即是递归出口，递归结束的条件
#              2.找出递归条件，即是每次递归都使得原本的问题更简单


# 使用递归计算数组的和
def list_sum(alist):
    if len(alist) == 1:
        return alist[0]
    else:
        return alist[0] + list_sum(alist[1:])


# 使用递归计算数组长度
def list_len(alist):
    if len(alist) == 1:
        return 1
    else:
        return 1 + list_len(alist[1:])


# 使用递归找出列表中最大的数
#



if __name__ == '__main__':
    print(list_sum([1, 2, 3, 4]))
    print(list_len([1, 2, 3, 4]))
