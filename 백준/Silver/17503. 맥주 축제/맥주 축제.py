# 23-05-03
# 17503 : 맥주 축제

import sys
input = sys.stdin.readline
import heapq

N, M, K = map(int, input().split())         # 기간 N / 선호도 합 M / 맥주 종류 수 K
beers = []
for i in range(K):
    v, c = map(int, input().split())
    beers.append([v, c])
beers.sort(key=lambda x:(x[1], x[0]))

hq = []
sum_v = 0

for i in range(K):
    heapq.heappush(hq, beers[i][0])
    sum_v += beers[i][0]
    
    if len(hq) == N:
        if sum_v >= M:
            rs = beers[i][1]
            break
        else:
            sum_v -= heapq.heappop(hq)
else:
    print(-1)
    exit()
print(rs)