# 10845 : 큐

import sys
input = sys.stdin.readline
from collections import deque

def pushOne(X):
    _queue.append(X)

def popOne():
    if isEmpty() == 1:
        print(-1)
    else:
        print(_queue.popleft())

def queueSize():
    print(len(_queue))

def isEmpty():
    if _queue:
        return 0
    else:
        return 1

def frontQueue():
    if isEmpty() == 1:
        print(-1)
    else:
        print(_queue[0])

def backQueue():
    if isEmpty() == 1:
        print(-1)
    else:
        print(_queue[len(_queue) - 1])

N = int(input())
_queue = deque()

for _ in range(N):
    opr = list(input().split())
    
    if opr[0] == 'push':
        pushOne(opr[1])
    if opr[0] == 'pop':
        popOne()
    if opr[0] == 'size':
        queueSize()
    if opr[0] == 'empty':
        print(isEmpty())
    if opr[0] == 'front':
        frontQueue()
    if opr[0] == 'back':
        backQueue()