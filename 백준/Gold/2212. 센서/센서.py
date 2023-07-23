# 2212 : 센서

import sys
input = sys.stdin.readline

N = int(input())
K = int(input())
sensors = sorted(list(map(int, input().split())))

arr = []
for i in range(N - 1):
    arr.append(sensors[i + 1] - sensors[i])
arr.sort()

print(sum(arr[:N - K]))