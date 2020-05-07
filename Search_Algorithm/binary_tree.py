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


pre = []
tin = []
post = []


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
        pre.append(root.elem)
        print(root.elem, end=" ")
        self.preorder(root.lchild)
        self.preorder(root.rchild)

    def inorder(self, root):
        """递归实现中序遍历"""
        if root is None:
            return
        self.inorder(root.lchild)
        tin.append(root.elem)
        print(root.elem, end=" ")
        self.inorder(root.rchild)

    def postorder(self, root):
        """递归实现后续遍历"""
        if root is None:
            return
        self.postorder(root.lchild)
        self.postorder(root.rchild)
        post.append(root.elem)
        print(root.elem, end=" ")

    # 根据前序、中序求后续遍历
    def reConstructTree(self, pre, tin):
        """根据前序中序重构树,前提是假设树节点中的值都是不重复的"""
        if len(pre) == 0:
            return None
        else:

            root = Node(pre[0])
            root_index_in_tin = tin.index(pre[0])
            root.lchild = self.reConstructTree(pre[1:root_index_in_tin + 1], tin[0:root_index_in_tin])
            root.rchild = self.reConstructTree(pre[root_index_in_tin + 1:], tin[root_index_in_tin + 1:])
            return root


if __name__ == '__main__':
    tree = Tree()
    for i in range(10):
        tree.add(i)
    tree.preorder(tree.root)
    print()
    tree.inorder(tree.root)
    print()
    tree.postorder(tree.root)
    print()
    print(pre)
    print(tin)
    print(post)
    root = tree.reConstructTree(pre, tin)
    print(root)
    tree.postorder(root)
