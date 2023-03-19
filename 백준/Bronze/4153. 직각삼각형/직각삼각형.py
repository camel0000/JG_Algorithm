# 4153 : 직각삼각형

import sys
input = sys.stdin.readline

while 1:
    a, b, c = map(int, input().split())
    
    if a == 0 and b == 0 and c == 0:
        break
    
    if (a*a + b*b == c*c) or (b*b + c*c == a*a) or (a*a + c*c == b*b):
        print('right')
    else:
        print('wrong')