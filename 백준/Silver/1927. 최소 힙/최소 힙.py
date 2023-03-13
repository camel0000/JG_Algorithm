# 1927 : 최소 힙

import sys
input = sys.stdin.readline
import heapq

N = int(input())

heap = []

for _ in range(N):
    X = int(input())
    
    if X == 0:
        if len(heap):
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, X)