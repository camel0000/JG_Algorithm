# 10814 : 나이순 정렬

import sys
input = sys.stdin.readline

N = int(input())

info = []

for i in range(N):
    tmp = list(input().rstrip().split())
    tmp[0] = int(tmp[0])
    info.append(tmp)
    info[i].append(i)
    
info.sort(key=lambda x : (x[0], x[2]))

for i in range(N):
    print(info[i][0], info[i][1])