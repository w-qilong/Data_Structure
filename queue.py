#!/usr/bin/python3
# _*_coding:utf-8 _*_
# @Time    :2019/10/17 21:58
# @Author  :WuQilong
# @FileName: queue.py 队列

class Queue(object):
    """Define the Queue"""

    def __init__(self):
        self.__list = []

    def enqueue(self, item):
        """Add a item to the top of queue"""

        self.__list.append(item)

    def dequeue(self):
        """Pop the item in the button of the queue"""
        return self.__list.pop()

    def is_empty(self):
        """Judge the queue is or not empty"""

        return not self.__list

    def size(self):
        """Return the length of queue"""

        return len(self.__list)


if __name__ == '__main__':
    queue = Queue()
    print(queue.is_empty())

    for i in range(1, 4):
        queue.enqueue(i)

    while not queue.is_empty():
        print(queue.dequeue())
