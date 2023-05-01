# 23-05-01
# 7571 : 점 모으기

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
X, Y = [], []

for _ in range(M):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

X.sort()
Y.sort()
a, b = X[M // 2], Y[M // 2]

dist = 0
for i in range(M):
    dist += abs(X[i] - a) + abs(Y[i] - b)
print(dist)