#!/usr/bin/python3
# _*_coding:utf-8 _*_
# @Time    :2019/10/16 18:54
# @Author  :WuQilong
# @FileName: double_link_list.py

class Node(object):
    """Define the Node."""

    def __init__(self, item=None):
        self.elem = item
        self.prev = None
        self.next = None


class DoubleLinkList(object):
    """Define the double link list."""

    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        """Judge the single list is empty."""

        return self.__head is None

    def length(self):
        """Get the single list length."""

        cur = self.__head  # cur is used to traversing nodes
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """Travel the single list."""

        cur = self.__head
        while cur is not None:
            print(cur.elem, end=" ")
            cur = cur.next

    def add(self, item):
        """Add a Node to the head."""

        node = Node(item)
        node.next = self.__head
        self.__head = node
        node.next.prev = node

    def append(self, item):
        """Add a Node to the tail."""

        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next is not None:
                cur = cur.next
            cur.next = node
            node.prev = cur

    def insert(self, pos, item):
        """Insert a Node to the specified location."""

        if pos >= self.length():
            self.append(item)
        elif pos <= 0:
            self.add(item)
        else:
            node = Node(item)
            cur = self.__head
            count = 1
            while count < pos:
                cur = cur.next
                count += 1
            node.next = cur.next
            cur.next = node


