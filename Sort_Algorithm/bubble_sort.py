#!/usr/bin/python3
# _*_coding:utf-8 _*_
# @Time    :2019/10/19 14:40
# @Author  :WuQilong
# @FileName:bubble_sort.py 冒泡排序改进版 最优时间复杂度O(n) 最差复杂度O(n^2) 稳定


def bubble_sort(alist):
    for j in range(len(alist) - 1, 0, -1):  # j指的是每次排序需要进行元素比较的次数
        count = 0  # 记录元素交换的次数
        for i in range(j):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
                count += 1
        if count == 0:  # 如果count为0，说明输入数列是有序的，直接跳出循环
            break
    return alist


if __name__ == '__main__':
    arr = [3, 1, 4, 2, 7, 8, 6, 5, 9]
    print("After sorted: %s" % bubble_sort(arr))
