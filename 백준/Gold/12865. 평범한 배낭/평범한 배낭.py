# 12865 : 평범한 배낭

import sys
input = sys.stdin.readline

N, K = map(int, input().split())

dp = [[0] * (K + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    weight, value = map(int, input().split())    # 무게, 가치
    
    for j in range(1, K + 1):
        if j - weight >= 0:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight] + value)
        else:
            dp[i][j] = dp[i - 1][j]
            
print(dp[-1][-1])