# 11053 : 가장 긴 증가하는 부분 수열

import sys
input = sys.stdin.readline

N = int(input())
seq = list(map(int, input().split()))

dp = [0 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if seq[i] > seq[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1

# print(seq)
# print(dp)

print(max(dp))