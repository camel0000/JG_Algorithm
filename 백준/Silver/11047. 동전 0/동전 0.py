# 11047 : 동전 0

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]

coins.sort(reverse=True)

cnt = 0

for coin in coins:
    if coin > K:
        continue
    cnt += (K // coin)
    K %= coin
    
print(cnt)