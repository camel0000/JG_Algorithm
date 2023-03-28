# 1010 : 다리 놓기

import sys
input = sys.stdin.readline
import math

for _ in range(int(input())):
    west, east = map(int, input().split())  # west <= east

    E = 1
    W = 1

    E = math.factorial(east) // math.factorial(east - west)
    W = math.factorial(west)
    print(E // W)