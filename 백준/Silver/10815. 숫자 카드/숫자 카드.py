# 10815 : 숫자 카드

import sys
input = sys.stdin.readline

N = int(input())
cards = set(map(int, input().split()))

M = int(input())
numbers = list(map(int, input().split()))

for n in numbers:
    if n in cards:
        print(1, end=' ')
    else:
        print(0, end=' ')