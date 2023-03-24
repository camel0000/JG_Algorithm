# 9251 : LCS

import sys
input = sys.stdin.readline
from itertools import combinations

str1 = list(input().rstrip())
str2 = list(input().rstrip())

h, w = len(str1), len(str2)
table = [[0] * (w + 1) for _ in range(h + 1)]

for i in range(1, h + 1):
    for j in range(1, w + 1):
        if str1[i - 1] == str2[j - 1]:
            table[i][j] = table[i - 1][j - 1] + 1
        else:
            table[i][j] = max(table[i][j - 1], table[i - 1][j])
print(table[-1][-1])