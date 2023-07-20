# 1963 : 소수 경로

import sys
input = sys.stdin.readline
from collections import deque

def isPrime(num):
    if num == 1:
        return 0
    for i in range(2, int(num**1/2) + 1):
        if num % i == 0:
            return 0
    return 1

def bfs(A, B):
    q = deque()
    q.append((A, 0))
    while q:
        num, count = q.popleft()
        if num == B:
            print(count)
            return
        for i in range(4):
            for j in range(10):
                new_num = list(str(num))
                new_num[i] = str(j)
                new_num = int(''.join(new_num))
                
                if 1000 <= new_num and not visited[new_num] and prime[new_num]:
                    visited[new_num] = 1
                    q.append((new_num, count + 1))

prime = [0]
for i in range(1, 10000):
    prime.append(isPrime(i))

for _ in range(int(input())):
    A, B = map(int, input().split())
    
    visited = [0] * 10000
    visited[A] = 1
    bfs(A, B)