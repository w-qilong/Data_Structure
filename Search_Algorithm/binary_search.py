#!/usr/bin/python3
# _*_coding:utf-8 _*_
# @Time    :2019/10/20 18:32
# @Author  :WuQilong
# @FileName:binary_search.py 二分查找，使用递归实现,只能用于有序顺序表查找,最优时间复杂度O(1),最坏时间复杂度O(logn)


def binary_search(alist, item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist) // 2
        if alist[midpoint] == item:
            return True
        else:
            if item < alist[midpoint]:
                return binary_search(alist[:midpoint], item)
            else:
                return binary_search(alist[midpoint + 1:], item)


if __name__ == '__main__':
    arr = [0, 1, 2, 3, 4, 5, 6, 7]
    print(binary_search(arr, 2))
    print(binary_search(arr, 8))