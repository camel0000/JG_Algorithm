# 10250 : ACM 호텔

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    h, w, n = map(int, input().split())
    
    ho = 1
    
    while n > h:
        n = n - h
        ho += 1
    
    print(n * 100 + ho)