# 16120 : PPAP

import sys
input = sys.stdin.readline

br = list(input().rstrip())
stack = []

for i in range(len(br)):
    stack.append(br[i])
    
    if len(stack) >= 4 and stack[-1] == 'P':
        # print(i)
        if stack[-1] == 'P':
            if stack[-2] == 'A':
                if stack[-3] == 'P':
                    if stack[-4] == 'P':
                        stack.pop()
                        stack.pop()
                        stack.pop()
                        stack.pop()
                        stack.append('P')

# print(stack)
if len(stack) == 1 and stack[0] == 'P':
    print('PPAP')
else:
    print('NP')