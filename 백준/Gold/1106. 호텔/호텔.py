# 1106_03 : 호텔

import sys
input = sys.stdin.readline

C, N = map(int, input().split())
dp = [[0] * (100 * C + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    cost, person = map(int, input().split())
        
    for j in range(1, 100 * C + 1): 
        if j - cost >= 0:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - cost] + person)
        else:
            dp[i][j] = dp[i - 1][j]

for j in range(1, 100 * C + 1):
    if dp[N][j] >= C:
        print(j)
        break