# -*- encoding: utf-8 -*-
"""
@File    : 寻找数组中位数.py
@Time    : 2020/5/2 16:17
@Author  : WuQilong
@Email   : 1528625919@qq.com
@Software: PyCharm
"""


def findMedianSortedArrays(nums1, nums2) -> float:
    merge = nums1 + nums2
    merge.sort()
    mid = len(merge) // 2
    if len(merge) // 2 == 0:
        return (merge[mid] + merge[mid - 1]) / 2
    else:
        return merge[mid]


if __name__ == '__main__':
    findMedianSortedArrays([1, 2, 3], [4, 5, 6, 7])
