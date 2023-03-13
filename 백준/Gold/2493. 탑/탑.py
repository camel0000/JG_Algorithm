# 2493 : 탑

# 1 <= N <= 500,000(50만)으로 O(N) ~ O(NlogN) 정도의 시간...?

import sys
input = sys.stdin.readline

N = int(input())
top = list(map(int, input().split()))

_stack = []
rs = [0 for _ in range(N)]

for i in range(N):
    t = top[i]
    
    while _stack and top[_stack[-1]] < t:   # 현재 탑 기준, 레이저를 받아줄 탑이 좌측에 없으면, 스택을 비워줘야 함
        _stack.pop()
    if _stack:                  # while을 통과했음에도, 스택이 비어있지 않다는 것은, 현재 탑의 레이저를 받을 탑이 좌측에 존재한다는 것
        rs[i] = _stack[-1] + 1
    _stack.append(i)                        # 스택에 현재 탑의 높이를 저장하여, 뒤에 비교할 수 있도록 함
        
print(' '.join(map(str, rs)))