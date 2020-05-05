#!/usr/bin/python3
# _*_coding:utf-8 _*_
# @Time    :2019/10/20 17:58
# @Author  :WuQilong
# @FileName:quick_sort.py 快速排序，时间复杂度为O(nlogn)

import random


# 对于快速排序，使用的是分而治之的思想，选用一个基准值，将原序列分为比基准值小的和比基准值大的两部分，在分成的小的序列上继续使用该方法，
# 直到序列的长度为空或长度为1，再将该序列按顺序拼接即可
def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


nums = []
for i in range(10):
    nums.append(random.randint(1, 10))
print("the raw nums is:", nums)
print("the sorted nums is:", quick_sort(nums))
