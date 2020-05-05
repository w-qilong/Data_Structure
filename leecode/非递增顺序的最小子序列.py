# -*- encoding: utf-8 -*-
"""
@File    : 非递增顺序的最小子序列.py
@Time    : 2020/5/4 9:24
@Author  : WuQilong
@Email   : 1528625919@qq.com
@Software: PyCharm
"""

"""
输入：nums = [4,3,10,9,8]
输出：[10,9] 
解释：子序列 [10,9] 和 [10,8] 是最小的、满足元素之和大于其他各元素之和的子序列。但是 [10,9] 的元素之和最大。 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-subsequence-in-non-increasing-order
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
"""
找出数组中最大值
判断最大值和其余值的和的大小，如果大于，停止循环，不然重复上述步骤
"""


def minSubsequence(num):
    if len(num) == 1:
        return num
    else:
        num.sort()
        max_child = []

        while sum(max_child) <= sum(num):
            max_value = num[-1]
            max_child.append(max_value)
            num.pop()
        return max_child


if __name__ == '__main__':
    print(minSubsequence([4,3,10,9,8]
                         ))
