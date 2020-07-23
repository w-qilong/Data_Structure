# -*- encoding: utf-8 -*-
"""
@File    : 使用两个栈实现队列.py
@Time    : 2020/5/10 10:19
@Author  : WuQilong
@Email   : 1528625919@qq.com
@Software: PyCharm
"""


class Queue():
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, item):
        self.stack1.append(item)

    def pop(self):
        if not self.stack1 and not self.stack2:
            return
        else:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()



if __name__ == '__main__':
    queue=Queue()
    for i in range(10):
        queue.push(i)
    print(queue.pop())
