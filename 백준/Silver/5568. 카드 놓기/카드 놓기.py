# 5568 : 카드 놓기

import sys
input = sys.stdin.readline
from itertools import permutations

n = int(input())
k = int(input())
A = [input().rstrip() for _ in range(n)]    # 문자열로 입력 받아야 후에 합치기 작업 가능

R = set()       # 뒤의 코드에서 중복 제거를 위해 set 자료형에 담을 준비

for p in permutations(A, k):    # permutations(n, k) == nCk (순열)
    R.add(''.join(p))           # 문자열 합치기 ''.join(x)
print(len(R))