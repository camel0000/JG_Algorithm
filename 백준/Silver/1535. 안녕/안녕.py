# 1535 : 안녕

import sys
input = sys.stdin.readline

N = int(input())
lose = [0] + list(map(int, input().split()))
gain = [0] + list(map(int, input().split()))

dp = [[0] * (100 + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, 100 + 1):
        if j - lose[i] >= 0:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - lose[i]] + gain[i])
        else:
            dp[i][j] = dp[i - 1][j]
            
print(dp[-1][99])