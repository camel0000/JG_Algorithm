# 2812 : 크게 만들기

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
num_list = list(map(int, str(input().rstrip())))

_stack = []

for i in num_list:
    while _stack and _stack[-1] < i and K > 0:
        _stack.pop()
        K -= 1
    _stack.append(i)

if K > 0:
    print(''.join(map(str, _stack[:-K])))
else:
    print(''.join(map(str, _stack)))