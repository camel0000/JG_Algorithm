# 8980 : 택배

import sys
input = sys.stdin.readline

N, C = map(int, input().split())
M = int(input())

info = []
for _ in range(M):
    info.append(list(map(int, input().split())))
info.sort(key=lambda x: x[0])
for i in range(M):
    info[i].append(info[i][2])

truck = 0
total_boxes = 0

for i in range(1, N + 1):
    # 내릴 것 있는지 체크
    for j in range(M):
        if info[j][1] == i:
            truck -= info[j][3]
    # 채울 것 있는지 체크
    for j in range(M):
        if truck >= C:
            break
        
        if info[j][0] == i:
            if C - truck < info[j][2]:
                info[j][2] -= (C - truck)
                temp = C - truck
                truck = C
                total_boxes += temp
                continue
            if C - truck >= info[j][2]:
                truck += info[j][2]
                total_boxes += info[j][2]
                info[j][2] = 0
print(total_boxes)