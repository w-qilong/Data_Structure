#!/usr/bin/python3
# _*_coding:utf-8 _*_
# @Time    :2019/10/20 18:12
# @Author  :WuQilong
# @FileName:merge_sort.py


def merge_sort(array):
    """归并排序"""

    length = len(array)

    if length <= 1:
        return array

    mid = length // 2

    left_arr = merge_sort(array[0:mid])  # 采用归并排序后形成的新序列
    right_arr = merge_sort(array[mid:])

    # 将两个新的自序列合并成一个新的整体
    left, right = 0, 0
    result = []

    while left < len(left_arr) and right < len(right_arr):

        if left_arr[left] < right_arr[right]:
            result.append(left_arr[left])
            left += 1
        else:
            result.append(right_arr[right])
            right += 1

    result += left_arr[left:]
    result += right_arr[right:]

    return result


if __name__ == '__main__':
    arr = [22, 55, 77, 99, 33, 44, 11]
    print(arr)  # [22, 55, 77, 99, 33, 44, 11]
    print(merge_sort(arr))  # [11, 22, 33, 44, 55, 77, 99]
