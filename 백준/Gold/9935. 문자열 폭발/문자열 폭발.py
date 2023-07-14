# 9935 : 문자열 폭발

import sys
input = sys.stdin.readline

_str = input().strip()
explosion = input().strip()

_stack = []

for s in _str:
    _stack.append(s)
    
    if ''.join(_stack[-len(explosion):]) == explosion:
        for _ in range(len(explosion)):
            _stack.pop()

if _stack:
    print(''.join(_stack))
else:
    print("FRULA")