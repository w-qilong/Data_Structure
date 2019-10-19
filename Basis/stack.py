#!/usr/bin/python3
# _*_coding:utf-8 _*_
# @Time    :2019/10/17 21:34
# @Author  :WuQilong
# @FileName: stack.py 栈


class Stack(object):
    """Define the Stack class."""

    def __init__(self):
        self.__list = []  # Init a list to save data

    def push(self, item):
        """Add data to the stack top"""

        self.__list.append(item)

    def pop(self):
        """Pop the top item of stack"""

        return self.__list.pop()

    def peek(self):
        """Return the top value of stack"""

        if self.__list:
            return self.__list[-1]
        else:
            return None

    def is_empty(self):
        """Judge the stack is or not empty"""

        return not self.__list

    def size(self):
        """Get the length of stack"""

        return len(self.__list)


if __name__ == '__main__':
    stack = Stack()
    print(stack.is_empty())
    for i in range(4):
        stack.push(i)
    print(stack.pop())
    print(stack.peek())
    print(stack.size())
