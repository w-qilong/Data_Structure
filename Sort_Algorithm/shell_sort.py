#!/usr/bin/python3
# _*_coding:utf-8 _*_
# @Time    :2019/10/19 18:09
# @Author  :WuQilong
# @FileName:shell_sort.py 希尔排序


def shell_sort(alist):
    n = len(alist)
    gap = int(n / 2)

    while gap > 0:
        for i in range(gap, n):
            temp = alist[i]
            j = i
            while j >= gap and alist[j - gap] > temp:
                alist[j] = alist[j - gap]
                j -= gap
            alist[j] = temp
        gap = int(gap / 2)
    return alist


if __name__ == '__main__':
    arr = [10, 3, 4, 2, 7, 8, 6, 5, 9]
    print("After sorted: %s" % shell_sort(arr))
