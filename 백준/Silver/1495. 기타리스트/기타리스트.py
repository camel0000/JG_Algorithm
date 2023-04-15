# 23-04-14
# 1495 : 기타리스트

import sys
input = sys.stdin.readline
from collections import deque

N, S, M = map(int, input().split())
V = list(map(int, input().split()))

v_record = [set() for _ in range(N)]
max_v = S
rs = -1

q = deque()
q.append((S, 0))

while q:
    v_pre, idx = q.popleft()
    
    if idx < len(V):
        n_v1 = v_pre + V[idx]
        n_v2 = v_pre - V[idx]

        if 0 <= n_v1 <= M:
            if n_v1 not in v_record[idx]:
                q.append((n_v1, idx + 1))
                v_record[idx].add(n_v1)
        if 0 <= n_v2 <= M:
            if n_v2 not in v_record[idx]:
                q.append((n_v2, idx + 1))
                v_record[idx].add(n_v2)
    else:
        rs = max(rs, v_pre)

print(rs)