# 10162 : 전자레인지

import sys
input = sys.stdin.readline

T = int(input())
A, B, C = 300, 60, 10
count_A = count_B = count_C = 0

if T >= A:
    while T > 0:
        T -= A
        count_A += 1
        
        if T < A:
            break

if T >= B:
    while T > 0:
        T -= B
        count_B += 1
        
        if T < B:
            break

if T >= C:
    while T > 0:
        T -= C
        count_C += 1
        
        if T < C:
            break

if T > 0:
    print(-1)
elif T == 0:
    print(count_A, count_B, count_C)
else:
    print(-1)