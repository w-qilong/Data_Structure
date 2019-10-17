#!/usr/bin/python3
# _*_coding:utf-8 _*_
# @Time    :2019/10/17 22:17
# @Author  :WuQilong
# @FileName: double_ended_queue.py 双端队列

class Dequeue(object):
    """Define the Dequeue"""

    def __init__(self):
        self.__list = []

    def add_front(self, item):
        """Add a item to the front of queue"""

        self.__list.insert(0, item)

    def add_rear(self, item):
        """Add a item to the end of queue"""

        self.__list.append(item)

    def pop_front(self):
        """Pop the item in the front of the queue"""

        return self.__list.pop(0)

    def pop_rear(self):
        """Pop the item in the end of the queue"""

        return self.__list.pop()

    def is_empty(self):
        """Judge the queue is or not empty"""

        return not self.__list

    def size(self):
        """Return the length of queue"""

        return len(self.__list)
