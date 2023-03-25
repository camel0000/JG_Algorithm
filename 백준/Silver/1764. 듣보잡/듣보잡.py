# 1764 : 듣보잡

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

same = set()

for _ in range(N):
    not_heard = input().rstrip()
    same.add(not_heard)

cnt_tmp = N     # same 집합의 원소 개수 갱신 용
cnt = 0

rs = []

for _ in range(M):
    not_saw = input().rstrip()
    same.add(not_saw)
    if len(same) == cnt_tmp:
        rs.append(not_saw)
    else:
        cnt_tmp += 1

rs.sort()
print(len(rs))
for i in range(len(rs)):
    print(rs[i])