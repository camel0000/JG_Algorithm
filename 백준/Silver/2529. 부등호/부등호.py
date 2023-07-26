# 2529 : 부등호

import sys
input = sys.stdin.readline

def check(i, j, k):
    if k == "<":
        return i < j
    else:
        return i > j

def solve(depth, S):
    global max_answer, min_answer
    
    if depth == k + 1:
        if len(min_answer) == 0:
            min_answer = S
        else:
            max_answer = S
        return
    
    for i in range(10):
        if not visited[i]:
            if depth == 0 or check(S[-1], str(i), signs[depth - 1]):
                visited[i] = 1
                solve(depth + 1, S + str(i))
                visited[i] = 0

k = int(input())
signs = list(input().split())

visited = [0] * 10
max_answer = ""
min_answer = ""

solve(0, "")
print(max_answer)
print(min_answer)