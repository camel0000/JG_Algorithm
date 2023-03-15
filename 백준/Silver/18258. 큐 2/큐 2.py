# 18258_02 : 큐 2

import sys
input = sys.stdin.readline
from collections import deque

def pushQueue(X):
    queue.append(X)
    return

def popQueue():
    if not queue:
        print(-1)
    else:
        print(queue.popleft())
    return

def printSize():
    print(len(queue))
    return

def isEmpty():
    if not queue:
        return 1
    else:
        return 0

def printFront():
    if isEmpty() == 1:
        print(-1)
    else:
        print(queue[0])

def printBack():
    if isEmpty() == 1:
        print(-1)
    else:
        print(queue[-1])


N = int(input())
queue = deque()

for _ in range(N):
    op = input().rstrip().split()

    if op[0] == 'push':
        pushQueue(op[1])

    if op[0] == 'pop':
        popQueue()

    if op[0] == 'size':
        printSize()

    if op[0] == 'empty':
        print(isEmpty())

    if op[0] == 'front':
        printFront()

    if op[0] == 'back':
        printBack()