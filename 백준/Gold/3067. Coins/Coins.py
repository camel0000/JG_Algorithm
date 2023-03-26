# 9084_02 : 동전

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    coins = list(map(int, input().split()))
    M = int(input())

    dp = [0] * (M + 1)
    dp[0] = 1

    for coin in coins:
        for j in range(1, M + 1):
            if j - coin >= 0:
                dp[j] += dp[j - coin]
    print(dp[M])