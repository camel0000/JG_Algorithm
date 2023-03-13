# 1715 : 카드 정렬하기

import sys
input = sys.stdin.readline
import heapq

N = int(input())

heap = []
for _ in range(N):
    X = int(input())
    heapq.heappush(heap, X)

tmp1 = tmp2 = 0
sum_tmp = 0
total = 0

for _ in range(N - 1):
    tmp1 = heapq.heappop(heap)
    tmp2 = heapq.heappop(heap)
    
    sum_tmp = tmp1 + tmp2
    
    heapq.heappush(heap, sum_tmp)
    
    total += sum_tmp
    
print(total)