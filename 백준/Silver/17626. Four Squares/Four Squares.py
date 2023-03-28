# 17626 : Four Squares

import sys
input = sys.stdin.readline

# DP
N = int(input())
square_num = [i*i for i in range(1, 224)]
dp = [0 for _ in range(N + 1)]
for i in range(1, N + 1):
    if i in square_num:
        dp[i] = 1
    else:
        dp[i] = min([dp[i - j] for j in square_num if i - j > 0]) + 1
print(dp[N])