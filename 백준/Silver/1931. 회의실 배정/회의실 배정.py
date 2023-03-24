# 1931 : 회의실 배정

import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
meetings = []

for _ in range(N):
    s, e = map(int, input().split())
    meetings.append((s, e))

# 끝나는 시간 기준으로 정렬    
meetings.sort(key=lambda x : (x[1], x[0]))

prev_meeting = meetings[0]
cnt = 1

for i in range(1, len(meetings)):
    if meetings[i][0] >= prev_meeting[1]:
        prev_meeting = meetings[i]
        cnt += 1
print(cnt)
