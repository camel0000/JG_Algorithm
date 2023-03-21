# 2294 : 동전 2

import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
types = [int(input()) for _ in range(n)]
types.sort()

q = deque()
visited = [0] * 100001
visited[0] = 1

for i in range(n):
    q.append((types[i], 1))
    visited[types[i]] = 1

while q:
    tmp_sum, tmp_cnt = q.popleft()
    
    if tmp_sum == k:
        print(tmp_cnt)
        exit()
    elif tmp_sum < k:
        for i in range(n):
            if visited[tmp_sum + types[i]] == 0:
                q.append((types[i] + tmp_sum, tmp_cnt + 1))
                visited[tmp_sum + types[i]] = 1
    else:   # tmp_sum > k:
        continue
    
print(-1)