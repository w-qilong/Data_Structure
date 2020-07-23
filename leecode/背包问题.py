# -*- encoding: utf-8 -*-
"""
@File    : 背包问题.py
@Time    : 2020/5/11 9:24
@Author  : WuQilong
@Email   : 1528625919@qq.com
@Software: PyCharm
"""
def pack1(w, v, C): #每个东西只能选择一次
    dp = [[0 for _ in range(C+1)] for _ in range(len(w)+1)]
    for i in range(1, len(w)+1):
        for j in range(1, C+1):
            if j < w[i-1]: #如果剩余容量不够新来的物体 直接等于之前的
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i-1]]+ v[i-1])
    return dp[len(w)][C]



weight = [2, 2, 6, 5, 4]
value = [3, 6, 5, 4, 6]
weight_most = 10




result = pack1(weight, value, weight_most)
print(result)
