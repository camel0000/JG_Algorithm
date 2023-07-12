# 1269 : 대칭 차집합

import sys
input = sys.stdin.readline

num_A, num_B = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

minus = len(A + B) - len(set(A + B))
print(len(set(A + B)) - minus)