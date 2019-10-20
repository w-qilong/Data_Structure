#!/usr/bin/python3
# _*_coding:utf-8 _*_
# @Time    :2019/10/20 17:58
# @Author  :WuQilong
# @FileName:quick_sort.py

import random


def quick_sort(nums, start, end):
    if start >= end:
        return
    low = start
    mid = nums[start]
    high = end
    while low < high:
        while low < high and mid <= nums[high]:
            high -= 1
        nums[low] = nums[high]
        while low < high and mid > nums[low]:
            low += 1
        nums[high] = nums[low]
    nums[low] = mid
    quick_sort(nums, start, low - 1)
    quick_sort(nums, low + 1, end)


nums = []
for i in range(10): nums.append(random.randint(1, 10))
print("the raw nums is:", nums)
quick_sort(nums, 0, len(nums) - 1)
print("the sorted nums is:", nums)
