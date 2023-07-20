# 6236 : 용돈 관리

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
cash = [int(input()) for _ in range(N)]

start = min(cash)
end = sum(cash)

while start <= end:
    charge = mid = (start + end) // 2
    num = 1
    
    for i in range(N):
        if charge < cash[i]:
            charge = mid
            num += 1
        charge -= cash[i]
    
    if num > M or mid < max(cash):
        start = mid + 1
    else:
        end = mid - 1
        K = mid
print(K)