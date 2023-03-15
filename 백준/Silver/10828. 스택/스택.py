# 10828_02 : 스택

import sys
input = sys.stdin.readline

def pushStack(X):
    _stack.append(X)
    return
def popStack():
    if isEmpty() == 1:
        print(-1)
    else:
        print(_stack.pop())
    return
def printSize():
    print(len(_stack))
    return
def isEmpty():
    if not _stack:
        return 1
    else:
        return 0
def printTop():
    if isEmpty() == 1:
        print(-1)
    else:
        print(_stack[-1])
    return

N = int(input())
_stack = []

for _ in range(N):
    op = input().split()
    
    if op[0] == 'push':
        pushStack(op[1])
    if op[0] == 'pop':
        popStack()
    if op[0] == 'size':
        printSize()
    if op[0] == 'empty':
        print(isEmpty())
    if op[0] == 'top':
        printTop()