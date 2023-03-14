# 2470_02 : 두 용액

import sys
input = sys.stdin.readline

N = int(input())
values = sorted(list(map(int, input().split())))

start = 0
end = N - 1

tmp = 2e9   # 최대는 10억, 최소는 -10억까지 가능하므로 tmp의 최대 범위인 20억으로 초기화
rs = 0

while start < end:
    _sum = values[start] + values[end]
    
    if abs(_sum) < tmp:
        tmp = abs(_sum)
        rs = (values[start], values[end])
        
    if _sum == 0:
        break
    elif _sum < 0:
        start += 1
    else:
        end -= 1
        
print(' '.join(map(str, rs)))