import sys
input = sys.stdin.readline
import heapq

N, K = map(int, input().split())
jews = [tuple(map(int, input().split())) for _ in range(N)]
bags = sorted([int(input()) for _ in range(K)])

# 무게순, 가격순으로 정렬
jews = sorted(jews)

# 가방 크기별로 고를 수 있는 보석을 heap에 저장
heap = []
j = 0
rs = 0
for i in range(K):
    while j < N and jews[j][0] <= bags[i]:
        heapq.heappush(heap, -jews[j][1])
        j += 1
    if heap:
        rs -= heapq.heappop(heap)

print(rs)