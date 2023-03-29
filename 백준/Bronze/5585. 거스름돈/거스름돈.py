# 5585 : 거스름돈

import sys
input = sys.stdin.readline

left = 1000 - int(input())
yen = [500, 100, 50, 10, 5, 1]

cnt = 0

for y in yen:
    if left < y:
        continue
    
    cnt += left // y
    left = left % y
print(cnt)