# 2628 : 종이 자르기

import sys
input = sys.stdin.readline

x, y = map(int, input().split())
X = [0, x, ]
Y = [0, y, ]

n = int(input())

for _ in range(n):
    a, b = map(int, input().split())    
    
    if a == 1:
        X.append(b)
        
    else:
        Y.append(b)

X.sort()
Y.sort()

sq = 0

for i in range(1, len(X)):
    for j in range(1, len(Y)):
        a = (X[i] - X[i - 1]) * (Y[j] - Y[j - 1])
        sq = max(sq, a)
print(sq)