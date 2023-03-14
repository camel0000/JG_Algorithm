# 1789 : 수들의 합

import sys
input = sys.stdin.readline

S = int(input())

start = 1
end = S

rs = 0

while start <= end:
    mid = (start + end) // 2
    
    if mid * (mid + 1) // 2 <= S:   # 1 ~ mid 까지의 합이 S보다 작으면,
        rs = mid
        start = mid + 1
    else:
        end = mid - 1
        
print(rs)