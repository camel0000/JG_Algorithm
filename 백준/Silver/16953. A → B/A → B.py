# 23-04-17
# 16953 : A -> B

import sys
input = sys.stdin.readline

A, B = map(int, input().split())

count = 0

while A < B:    
    if B % 10 == 1: # B의 마지막 숫자가 1일 경우
        B = B // 10
    elif B % 2 == 0:
        B = B // 2
    else:
        print(-1)
        exit()
        
    count += 1
    
if A == B:
    print(count + 1)
else:
    print(-1)