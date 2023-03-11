# 1920 : 수 찾기

# N의 범위가 100,000으로, O(nlogn)의 시간 안으로 풀어야 할 것으로 예상됨!
# 이분 탐색
# 이지만, 이분 탐색 학습 전이므로 일단 풀이

import sys
input = sys.stdin.readline

N = int(input())
A = set(map(int, input().split()))

M = int(input())
_list = list(map(int, input().split()))

for i in _list:
    if i in A:
        print(1)
    else:
        print(0)