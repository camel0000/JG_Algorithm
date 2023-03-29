# 1541_02 : 잃어버린 괄호

import sys
input = sys.stdin.readline

_list = list(input().rstrip())

mi = 0
tmp = 0
rs = 0

for x in _list:
    if x != '+' and x != '-':   # 숫자 합쳐서 정수형 화
        tmp *= 10
        tmp += int(x)
    
    if x == '-':
        if mi == 0:
            rs += tmp
            tmp = 0
            mi = 1
        else:
            rs -= tmp
            tmp = 0
    
    if x == '+':
        if mi == 0:
            rs += tmp
            tmp = 0        
        else:
            rs -= tmp
            tmp = 0

if mi == 0:
    rs += tmp
else:
    rs -= tmp

print(rs)