#!/usr/bin/python3
# _*_coding:utf-8 _*_
# @Time    :2019/10/19 17:17
# @Author  :WuQilong
# @FileName:insert_sort.py 插入排序，最坏时间复杂度O(n^2),最优时间复杂度O(n)


def insert_sort(alist):
    for j in range(1, len(alist)):
        i = j
        while i > 0:
            if alist[i] < alist[i - 1]:  # 当插入元素小于前一个元素的时候
                alist[i], alist[i - 1] = alist[i - 1], alist[i]
                i -= 1
            else:  # 当插入元素大于等于前一个元素的时候
                break
    return alist


if __name__ == '__main__':
    arr = [10, 3, 4, 2, 7, 8, 6, 5, 9]
    print("After sorted: %s" % insert_sort(arr))
