# 2217 : 로프

import sys
input = sys.stdin.readline

weights = []
for _ in range(int(input())):
    weights.append(int(input()))
weights.sort(reverse=True)

results = []
for i in range(len(weights)):
    results.append(weights[i] * (i + 1))

print(max(results))