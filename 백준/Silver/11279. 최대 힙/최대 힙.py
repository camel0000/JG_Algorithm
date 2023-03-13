# 11279 : 최대 힙

import sys
input = sys.stdin.readline
import heapq

N = int(input())
max_heap = []

for _ in range(N):
    X = int(input())
    
    if X:
        heapq.heappush(max_heap, -X)
    else:
        if not max_heap:
            print(0)
        else:
            print(-heapq.heappop(max_heap))