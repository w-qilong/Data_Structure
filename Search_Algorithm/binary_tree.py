#!/usr/bin/python3
# _*_coding:utf-8 _*_
# @Time    :2019/10/21 9:39
# @Author  :WuQilong
# @FileName:binary_tree.py 二叉树的实现，遍历，求深度等


class Node(object):
    """class BiNode provide interface to set up a BiTree Node and to interact"""

    def __init__(self, element=None, left=None, right=None):
        """set up a node """
        self.element = element
        self.left = left
        self.right = right

    def get_element(self):
        """return node.element"""
        return self.element

    def dict_form(self):
        """return node as dict form"""
        dict_set = {
            "element": self.element,
            "left": self.left,
            "right": self.right,
        }
        return dict_set

    def __str__(self):
        """when print a node , print it's element"""
        return str(self.element)


class Tree(object):
    """class BiTree provide interface to set up a BiTree and to interact"""

    def __init__(self, tree_node=None):
        """set up BiTree from BiNode and empty BiTree when nothing is passed"""
        self.root = tree_node

    def add_node_in_order(self, element):
        """add a node to existent BiTree in order"""
        node = Node(element)

        if self.root is None:
            self.root = node
        else:
            node_queue = list()
            node_queue.append(self.root)
            while len(node_queue):
                q_node = node_queue.pop(0)
                if q_node.left is None:
                    q_node.left = node
                    break
                elif q_node.right is None:
                    q_node.right = node
                    break
                else:
                    node_queue.append(q_node.left)
                    node_queue.append(q_node.right)

    def get_depth(self):
        """method of getting depth of BiTree"""
        if self.root is None:
            return 0
        else:
            node_queue = list()
            node_queue.append(self.root)
            depth = 0
            while len(node_queue):
                q_len = len(node_queue)
                while q_len:
                    q_node = node_queue.pop(0)
                    q_len = q_len - 1
                    if q_node.left is not None:
                        node_queue.append(q_node.left)
                    if q_node.right is not None:
                        node_queue.append(q_node.right)
                depth = depth + 1
            return depth

    def pre_traversal(self):
        """method of traversing BiTree in pre-order"""
        if self.root is None:
            return None
        else:
            node_stack = list()
            output_list = list()
            node = self.root
            while node is not None or len(node_stack):
                # if node is None which means it comes from a leaf-node' right,
                # pop the stack and get it's right node.
                # continue the circulating like this
                if node is None:
                    node = node_stack.pop().right
                    continue
                #  save the front node and go next when left node exists
                while node.left is not None:
                    node_stack.append(node)
                    output_list.append(node.get_element())
                    node = node.left
                output_list.append(node.get_element())
                node = node.right
        return output_list


if __name__ == '__main__':
    node = Node(5)
    print(node.dict_form())
    tree = Tree()
    for i in range(5):
        tree.add_node_in_order(i)
    print(tree.get_depth())
    print(tree.pre_traversal())
