# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        pre = None
        while pHead is not None:
            next = pHead.next
            pHead.next = pre
            pre = pHead
            pHead = next
        return pre