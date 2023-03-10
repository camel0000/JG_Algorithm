# 11279 : 최대 힙

import sys
input = sys.stdin.readline
import heapq

N = int(input())
array = []

for _ in range(N):
    x = int(input())
    
    if x:
        heapq.heappush(array, (-x, x))
    else:
        if not array:
            print(0)
        else:
            print(heapq.heappop(array)[1])