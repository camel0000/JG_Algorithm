# 1106 : 호텔

import sys
input = sys.stdin.readline

C, N = map(int, input().split())

maxCost = sys.maxsize
dp = [[maxCost] * (C + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    cost, num = map(int, input().split())
    
    for j in range(1, C + 1):
        k = 0
        dp[i][j] = dp[i - 1][j]
        
        while 1:
            if j - (k * num) > 0:
                dp[i][j] = min(dp[i][j], dp[i - 1][j - k * num] + k * cost)
            else:
                dp[i][j] = min(dp[i][j], k * cost)
                break
            k += 1

print(dp[-1][-1])