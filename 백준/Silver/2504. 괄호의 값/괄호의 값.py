# 2504 : 괄호의 값

import sys
input = sys.stdin.readline

p = list(str(input().rstrip()))

_stack = []
tmp = 1     # result에 더해주기 전 임시 변수
result = 0  # 결과 변수

for i in range(len(p)):
#   print('현재:', p[i], end=', ')  
    
  if p[i] == '(':
    tmp *= 2
    _stack.append(p[i])
    # print('tmp :', tmp, ', rs :', result)
    
  elif p[i] == '[':
    tmp *= 3
    _stack.append(p[i])
    # print('tmp :', tmp, ', rs :', result)

  elif p[i] == ')':
    if not _stack or _stack[-1] != '(':
      result = 0
      break
    if p[i - 1] == '(':
        result += tmp
    tmp //= 2
    _stack.pop()
    # print('tmp :', tmp, ', rs :', result)

    
  elif p[i] == ']':
    if not _stack or _stack[-1] != '[':
      result = 0
      break
    if p[i - 1] == '[':
        result += tmp
    tmp //= 3
    _stack.pop()
    # print('tmp :', tmp, ', rs :', result)

if _stack:
  print(0)
else:
  print(result)