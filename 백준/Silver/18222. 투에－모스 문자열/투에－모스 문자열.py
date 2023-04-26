# 23-04-26
# 18222 : 투에-모스 문자열

import sys
input = sys.stdin.readline
sys.setrecursionlimit(5000)

def solve(k):
    if k == 0:
        return 0
    if k == 1:
        return 1
    
    if k % 2:
        return 1 - solve(k // 2)
    else:
        return solve(k // 2)

k = int(input())
print(solve(k - 1))