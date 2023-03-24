# 1541 : 잃어버린 괄호

import sys
input = sys.stdin.readline

ex = list(input().rstrip())

minus = 0
stack = []


for i in range(len(ex)):
    if ex[i] == '0' and not stack:
        continue
    if ex[i] == '0' and stack[-1] == '+':
        continue
    if ex[i] == '0' and stack[-1] == '-':
        continue
    
    if ex[i] != '+' and ex[i] != '-':
        stack.append(ex[i])
    
    if ex[i] == '+':
        if minus == 1:
            stack.append('-')
        else:
            stack.append('+')
    
    if ex[i] == '-':
        minus = 1
        stack.append('-')

# print(''.join(map(str, stack)))
print(eval(''.join(map(str, stack))))