# 10000 : 원 영역

import sys
input = sys.stdin.readline
import heapq

N = int(input())

circles = []
for _ in range(N):
    x, r = map(int, input().split())
    end = x + r
    dist = 2 * r    
    circles.append((end, dist))
    
circles.sort()

h = []
cnt = 1

for i in range(N):
    end, dist = circles[i]
    start = end - dist
    can_fill = False
    last_point = end
    
    while h:
        e, d = heapq.heappop(h)
        e = -e
        if e <= start:
            heapq.heappush(h, (-e, d))
            break
        if e != last_point and e - d >= start:
            continue
        if e - d >= start:
            last_point = e - d
        if last_point == start:
            can_fill = True
    
    cnt += 1
    
    if can_fill:
        cnt += 1
    heapq.heappush(h, (-end, dist))

print(cnt)