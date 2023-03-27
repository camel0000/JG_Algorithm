# 2748_02 : 피보나치 수 2

import sys
input = sys.stdin.readline

N = int(input())

dp = [0 for _ in range(N + 1)]
dp[0] = 0
dp[1] = 1

for i in range(2, N + 1):
    dp[i] = dp[i - 2] + dp[i - 1]
print(dp[N])