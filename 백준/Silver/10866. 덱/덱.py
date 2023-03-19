# 10866 : 덱

import sys
input = sys.stdin.readline
from collections import deque

def pushFront(X):
    dq.appendleft(X)
    return
def pushBack(X):
    dq.append(X)
    return
def popFront():
    if isEmpty() == 1:
        print(-1)
    else:
        print(dq.popleft())
    return
def popBack():
    if isEmpty() == 1:
        print(-1)
    else:
        print(dq.pop())
    return
def dequeSize():
    return len(dq)
def isEmpty():
    if dequeSize() == 0:
        return 1
    else:
        return 0
def printFront():
    if isEmpty() == 1:
        print(-1)
    else:
        print(dq[0])
def printBack():
    if isEmpty() == 1:
        print(-1)
    else:
        print(dq[-1])


N = int(input())
dq = deque()

for _ in range(N):
    st = input().rstrip().split()
    
    if st[0] == 'push_front':
        pushFront(st[1])
    if st[0] == 'push_back':
        pushBack(st[1])
    if st[0] == 'pop_front':
        popFront()
    if st[0] == 'pop_back':
        popBack()
    if st[0] == 'size':
        print(dequeSize())
    if st[0] == 'empty':
        print(isEmpty())
    if st[0] == 'front':
        printFront()
    if st[0] == 'back':
        printBack()