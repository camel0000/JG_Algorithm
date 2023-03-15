# 2470_03 : 두 용액

import sys
input = sys.stdin.readline

N = int(input())
values = sorted(list(map(int, input().split())))

# 범위를 포인터로 잡기
start = 0   # 첫 값
end = N - 1 # 마지막 값

tmp = 2e9

while start < end:
    total = values[start] + values[end]
    
    if abs(total) < tmp:
        tmp = abs(total)
        rs = (values[start], values[end])
    
    if total == 0:
        break
    elif total > 0:
        end -= 1
    else:
        start += 1
        
print(' '.join(map(str, rs)))