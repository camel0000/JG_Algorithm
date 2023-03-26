# 11053 : 가장 긴 증가하는 부분 수열

import sys
input = sys.stdin.readline

# O(NlogN) 풀이

from bisect import bisect_left

N = int(input())
seq = list(map(int, input().split()))

dp = [seq[0]]

for i in range(1, N):
    if dp[-1] > seq[i]:
        idx = bisect_left(dp, seq[i])
        dp[idx] = seq[i]
    elif dp[-1] < seq[i]:
        dp.append(seq[i])

print(len(dp))