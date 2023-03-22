# 1948 : 임계경로

import sys
input = sys.stdin.readline
from collections import deque

N = int(input())    # N: 도시의 개수
M = int(input())    # M: 도로의 개수

time = [0] * (N + 1)
in_degree = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]
cnt = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    in_degree[b] += 1

src, dst = map(int, input().split())

q = deque()
q.append(src)

while q:
    now = q.popleft()   # now: 도시, cnt: 지나온 경로의 개수
    
    # i[0]: 비용, i[1]: 도시
    for i in graph[now]:
        in_degree[i[1]] -= 1
        # 비용이 갱신 될 때
        if time[i[1]] < time[now] + i[0]:
            time[i[1]] = time[now] + i[0]
            # 달려야 하는 도로의 수 갱신
            cnt[i[1]] = [now]
        elif time[i[1]] == time[now] + i[0]:
            cnt[i[1]].append(now)

        # 선행 도로를 모두 지나갔을 때
        if in_degree[i[1]] == 0:
            q.append(i[1])

q = deque([dst])
route = set()

while q:
    now = q.popleft()
    for x in cnt[now]:
        if (now, x) not in route:
            route.add((now, x))
            q.append(x)

print(time[dst])
print(len(route))