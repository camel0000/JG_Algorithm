# 23-04-07
# 23757 : 아이들과 선물 상자

import sys
input = sys.stdin.readline
import heapq

box, boy = map(int, input().split())
boxes = list(map(int, input().split()))
boys = list(map(int, input().split()))

x = []
for gift in boxes:
    heapq.heappush(x, -gift)

count = 0
for boy in boys:
    gift = -heapq.heappop(x)
    
    if gift < 1: break
    
    if gift < boy: continue
    else:
        gift -= boy
        heapq.heappush(x, -gift)
        count += 1
        
if count == len(boys): print(1)
else: print(0)