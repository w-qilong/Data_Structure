#!/usr/bin/python3
# _*_coding:utf-8 _*_
# @Time    :2019/10/17 19:04
# @Author  :WuQilong
# @FileName: single_cycle_link_list.py 单向循环链表


class Node(object):
    """Define the Node class."""

    def __init__(self, elem):
        self.elem = elem
        self.next = None


class SingleCycleLinkList(object):
    """Define the single cycle link list."""

    def __init__(self, node=None):
        self.__head = node
        if node:
            node.next = node

    def is_empty(self):
        """Judge the single list is empty."""

        return self.__head is None

    def length(self):
        """Get the single list length."""

        if self.is_empty():
            return 0
        cur = self.__head  # cur is used to traversing nodes
        count = 1
        while cur.next is not self.__head:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """Travel the single list."""

        cur = self.__head
        while cur.next is not self.__head:
            print(cur.elem, end=" ")
            cur = cur.next
        print(cur.elem, end=" ")  # Print the last Node

    def add(self, item):
        """Add a Node to the head."""

        node = Node(item)
        if self.__head is None:
            self.__head = node
            node.next = Node
        else:
            cur = self.__head
            while cur.next is not self.__head:
                cur = cur.next
            node.next = self.__head
            self.__head = node
            cur.next = node

    def append(self, item):
        """Add a Node to the tail."""

        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next is not self.__head:
                cur = cur.next

            cur.next = node
            node.next = self.__head

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

    def search(self, item):
        """Search the Node from single list"""

        cur = self.__head
        if cur.elem == item:
            return True
        while cur is not self.__head:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        if cur.elem is item:
            return True
        return False

    def remove(self, item):
        """Remove the item Node."""

        if self.is_empty():
            return
        cur = self.__head
        pre = None
        while cur.next is not self.__head:
            if cur.elem == item:
                if cur == self.__head:  # If the item is the first Node
                    rear = self.__head
                    while rear.next is not self.__head:
                        rear = rear.next
                    self.__head = cur.next
                    rear.next = self.__head
                else:  # If the Node is middle Node
                    pre.next = cur.next
                return
            else:
                pre = cur
                cur = cur.next
        if cur.elem == item:  # If the node is the last one
            if cur == self.__head:  # If the node just has one Node
                self.__head = None
            else:
                pre.next = cur.next


if __name__ == '__main__':
    single_cycle = SingleCycleLinkList()
    for i in range(1, 4):
        single_cycle.append(i)
    single_cycle.travel()
    single_cycle.add(4)
    single_cycle.travel()
    print(single_cycle.search(1))
    single_cycle.remove(1)
    single_cycle.travel()
