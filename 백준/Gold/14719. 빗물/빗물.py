# 23-04-15
# 14719 : 빗물

import sys
input = sys.stdin.readline

h, w = map(int, input().split())
heights = list(map(int, input().split()))   # 각 원소 0 ~ h
maps = [[0] * w for _ in range(h)]

for i in range(w):
    for j in range(heights[i]):
        maps[h - j - 1][i] = 1

left = right = 0

for i in range(h):
    for j in range(w):
        left = right = 0
        
        if maps[i][j] == 0:
            for a in range(0, j):
                if maps[i][a] == 1:
                    left += 1
                    break
            for a in range(j + 1, w):
                if maps[i][a] == 1:
                    right += 1
                    break
            if left == 1 and right == 1:
                maps[i][j] = 2

rs = 0
for i in range(h):
    for j in range(w):
        if maps[i][j] == 2:
            rs += 1
print(rs)