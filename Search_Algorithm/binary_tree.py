#!/usr/bin/python3
# _*_coding:utf-8 _*_
# @Time    :2019/10/21 9:39
# @Author  :WuQilong
# @FileName:binary_tree.py 二叉树的实现，遍历，求深度等,以下实现为完全二叉树


class Node(object):
    """节点类"""

    def __init__(self, elem):
        self.elem = elem
        self.lchild = None
        self.rchild = None


class Tree(object):
    """树类"""

    def __init__(self, root=None):
        self.root = root

    def add(self, elem):
        """为树添加节点"""
        node = Node(elem)
        # 如果树是空的，则对根节点赋值
        if self.root is None:
            self.root = node
        else:
            queue = [self.root]
            # 对已有的节点进行层次遍历
            while queue:
                # 弹出队列的第一个元素
                cur = queue.pop(0)
                if cur.lchild is None:
                    cur.lchild = node
                    break
                elif cur.rchild is None:
                    cur.rchild = node
                    break
                else:
                    # 如果左右子树都不为空，加入队列继续判断
                    queue.append(cur.lchild)
                    queue.append(cur.rchild)

    def preorder(self, root):
        """递归实现先序遍历"""
        if root is None:
            return
        print(root.elem, end=" ")
        self.preorder(root.lchild)
        self.preorder(root.rchild)

    def inorder(self, root):
        """递归实现中序遍历"""
        if root is None:
            return
        self.inorder(root.lchild)
        print(root.elem, end=" ")
        self.inorder(root.rchild)

    def postorder(self, root):
        """递归实现后续遍历"""
        if root is None:
            return
        self.postorder(root.lchild)
        self.postorder(root.rchild)
        print(root.elem, end=" ")


if __name__ == '__main__':
    tree = Tree()
    for i in range(10):
        tree.add(i)
    tree.preorder(tree.root)
    print()
    tree.inorder(tree.root)
    print()
    tree.postorder(tree.root)
