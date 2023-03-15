# 11279_02 : 최대 힙

import sys
input = sys.stdin.readline
import heapq

N = int(input())
heap = []

for _ in range(N):
    x = int(input())
    
    if x == 0:
        if not heap:
            print(0)
        else:
            print(-heapq.heappop(heap))
    else:
        heapq.heappush(heap, -x)