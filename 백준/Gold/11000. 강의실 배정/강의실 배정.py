# 11000 : 강의실 배정

import sys
input = sys.stdin.readline
import heapq

N = int(input())
times = sorted([tuple(map(int, input().split())) for _ in range(N)])

cnt = 0

room = []
heapq.heappush(room, times[0][1])

for time in times[1:]:
    if time[0] < room[0]:
        heapq.heappush(room, time[1])
    else:
        heapq.heappop(room)
        heapq.heappush(room, time[1])
print(len(room))