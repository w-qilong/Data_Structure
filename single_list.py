#!/usr/bin/python3
# _*_coding:utf-8 _*_
# @Time    :2019/10/15 14:17
# @Author  :WuQilong
# @FileName: single_list.py

class Node(object):
    """Define the Node class."""

    def __init__(self, elem):
        self.elem = elem
        self.next = None


class SingleLinkList(object):
    """Define the single list class."""

    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        """Judge the single list is empty."""

        return self.__head == None

    def length(self):
        """Get the single list length."""

        cur = self.__head  # cur is used to traversing nodes
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """Travel the single list."""

        cur = self.__head
        while cur != None:
            print(cur.elem, end=" ")
            cur = cur.next

    def append(self, item):
        """Add a Node to the tail."""

        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def add(self, item):
        """Add a Node to the head."""

        node = Node(item)
        node.next = self.__head
        self.__head = node

    def insert(self, pos, item):
        """Insert a Node to the specified location."""

        if pos >= self.length():
            self.append(item)
        elif pos <= 0:
            self.add(item)
        else:
            node = Node(item)
            pre = self.__head
            count = 1
            while count < pos:
                pre = pre.next
                count += 1
            node.next = pre.next
            pre.next = node

    def search(self, item):
        """Search the Node from single list"""

        cur = self.__head
        if cur.elem == item:
            return True
        while cur != None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False

    def remove(self, item):
        """Remove the item Node."""

        cur = self.__head
        pre = None
        while cur != None:
            if cur.elem == item:
                if cur == self.__head:  # If the item is the first Node
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next


if __name__ == '__main__':
    single_list = SingleLinkList()
    for i in range(1, 4):
        single_list.append(i)
    single_list.travel()
    single_list.remove(2)
    single_list.travel()
