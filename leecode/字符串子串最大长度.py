# -*- encoding: utf-8 -*-
"""
@File    : 字符串子串最大长度.py
@Time    : 2020/5/2 14:10
@Author  : WuQilong
@Email   : 1528625919@qq.com
@Software: PyCharm
"""


def lengthOfLongestSubstring(s: str) -> int:
    """
    st用来记录遍历过的字符的位置
    i为用来记录不重复子串的初始位置，如果在遍历过程中，出现了重复字符，就将i指针移动到重复字符的位置
    j用来遍历整个字符的指针
    ans用来记录最大子字符串的长度
    :param s:
    :return:
    """
    st = {}
    i, ans = 0, 0  # 初始化指针和子串长度
    for j in range(len(s)):  # 遍历字符
        if s[j] in st:  # 如果j指针指向已经出现过的字符
            i = max(st[s[j]], i)  # 调整i指针位置，使其指向重复的那个字符
        ans = max(ans, j - i + 1)  # 记录子串最大长度，j-i+1即是遍历过程中每个子串的长度
        st[s[j]] = j + 1  # 记录出现的每个字符的位置
    return ans


if __name__ == '__main__':
    s = "abcab"
    print(lengthOfLongestSubstring(s))
