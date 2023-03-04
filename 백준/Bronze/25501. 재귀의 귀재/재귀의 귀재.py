# 25501 : 재귀의 귀재

import sys
input = sys.stdin.readline

def recursion(S, l, r):    
    if l >= r:
        return 1
    elif S[l] != S[r]:
        return 0
    else:
        return recursion(S, l + 1, r - 1)

def isPalindrome(S):
    return recursion(S, 0, len(S) - 1)

def countNotRecursion(S, l, r):
    cnt = 0
    
    while S[l] == S[r]:
        cnt += 1
        l += 1
        r -= 1
    
    return cnt

T = int(input())

for _ in range(T):
    S = input().rstrip()
    p = isPalindrome(S)
    
    if p == 1:
        print(1, len(S) // 2 + 1)
    else:
        print(0, countNotRecursion(S, 0, len(S) - 1) + 1)