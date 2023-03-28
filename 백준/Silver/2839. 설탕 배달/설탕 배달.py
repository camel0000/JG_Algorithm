# 2839 : 설탕 배달

import sys
input = sys.stdin.readline

N = int(input())
x = N // 5

for i in range(x, -1, -1):
    y = N - (5 * i)
    
    if y % 3 != 0:
        continue
    
    print(i + (y // 3))
    exit()
    
print(-1)