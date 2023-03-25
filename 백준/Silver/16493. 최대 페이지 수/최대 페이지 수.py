# 16493 : 최대 페이지 수

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
chaps = []
dp = [[0] * (N + 1) for _ in range(M + 1)]

for i in range(1, M + 1):
    day, page = map(int, input().split())
    
    for j in range(1, N + 1):
        if j - day >= 0:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - day] + page)
        else:
            dp[i][j] = dp[i - 1][j]
            
print(dp[-1][-1])