# 13334 : 철로

import sys
input = sys.stdin.readline
import heapq

n = int(input())
locations = []
for _ in range(n):
    start, end = map(int, input().split())
    if start > end:
        start, end = end, start
    heapq.heappush(locations, (end, start))

d = int(input())

poss = []
rs = 0
cnt = 0

while locations:
    end, start = heapq.heappop(locations)
    
    if start >= end - d:
        heapq.heappush(poss, (start, end))
        cnt += 1
    
    while poss:
        s, e = heapq.heappop(poss)
        
        if s < end - d:
            cnt -= 1
        else:
            heapq.heappush(poss, (s, e))
            break
        
    rs = max(rs, cnt)

print(rs)