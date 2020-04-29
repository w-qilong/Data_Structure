#!/usr/bin/python3
# _*_coding:utf-8 _*_
# @Time    :2019/10/19 16:32
# @Author  :WuQilong
# @FileName:select_sort.py 选择排序 最优复杂度O(n^2) 没有优化方式 不稳定


def selection_sort(alist):
    for i in range(len(alist) - 1):  # 需要进行n-1次操作
        min_index = i  # 记录最小位置
        # 从i+1位置到末尾选择出最小的数据
        for j in range(i + 1, len(alist)):
            if alist[j] < alist[min_index]:
                min_index = j
        alist[i], alist[min_index] = alist[min_index], alist[i]
    return alist


if __name__ == '__main__':
    arr = [3, 3, 4, 2, 7, 8, 6, 5, 9]
    print("After sorted: %s" % selection_sort(arr))
