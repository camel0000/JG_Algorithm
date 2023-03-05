import sys
input = sys.stdin.readline

N = int(input())

mul = 1

for i in range(N, 0, -1):
    mul *= i
print(mul)