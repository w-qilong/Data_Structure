# -*- encoding: utf-8 -*-
"""
@File    : 判断二叉树两个二叉树是否是子结构.py
@Time    : 2020/5/10 22:03
@Author  : WuQilong
@Email   : 1528625919@qq.com
@Software: PyCharm
"""


class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if not pRoot1 or not pRoot2:
            return False
        return self.is_subtree(pRoot1, pRoot2) or self.HasSubtree(pRoot1.left, pRoot2) or self.HasSubtree(pRoot1.right,
                                                                                                          pRoot2)

    def is_subtree(self, A, B):
        if not B:
            return True
        if not A or A.val != B.val:
            return False
        return self.is_subtree(A.left, B.left) and self.is_subtree(A.right, B.right)
