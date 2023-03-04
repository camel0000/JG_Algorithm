# 1181 : 단어 정렬

import sys
input = sys.stdin.readline

N = int(input())
_list = []

for _ in range(N):
    _list.append(input().rstrip())

_list = list(set(_list))
_list.sort()
_list.sort(key=len)

for i in range(len(_list)):
    print(_list[i])