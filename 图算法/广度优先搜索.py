# -*- encoding: utf-8 -*-
"""
@File    : 广度优先搜索.py
@Time    : 2020/5/8 8:57
@Author  : WuQilong
@Email   : 1528625919@qq.com
@Software: PyCharm
"""
from collections import deque


# 广度优先搜索，在图中查找指定元素，常用于寻找最短路径,通常使用队列实现，在二叉树的遍历中也使用了该方法来遍历节点。
# 使用字典构造一个图,该图为有向图
def constructGraph():
    graph = {}
    graph["you"] = ["alice", "bob", "claire"]
    graph["bob"] = ["anuj", "peggy"]
    graph["alice"] = ["peggy"]
    graph["claire"] = ["thom", "jonny"]
    graph["anuj"] = []
    graph["peggy"] = []
    graph["thom"] = []
    graph["jonny"] = []
    return graph


def BbreadthFirstSearch(graph, you, name):
    """
    实现广度优先搜索
    :param graph:输入的图
    :param you: 查找起点(可以联想到在最短路径搜索中对应起点位置)
    :param name: 查找元素（对应终点位置）
    :return: True or False
    """
    que = deque()
    que += graph[you]
    searched = set()  # 使用集合记录已经查找过的顶点，防止死循环
    while que:
        curValue = que.popleft()
        if curValue not in searched:
            if curValue == name:
                return True
            else:
                que += graph[curValue]
                searched.add(curValue)
    return False


if __name__ == '__main__':
    graph = constructGraph()
    result = BbreadthFirstSearch(graph, 'you', 'thom')
    print(result)
