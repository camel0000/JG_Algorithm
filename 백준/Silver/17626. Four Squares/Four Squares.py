# 17626 : Four Squares

import sys
input = sys.stdin.readline
from math import sqrt
from itertools import combinations_with_replacement

N = int(input())
square_num_1 = [i*i for i in range(1, int(sqrt(N)) + 1)]
square_num_2 = [sum(k) for k in combinations_with_replacement(square_num_1, 2)]

if N in square_num_1:
    print(1)
    exit()
elif N in square_num_2:
    print(2)
    exit()
else:
    for sq in square_num_1:
        if N - sq in square_num_2:
            print(3)
            exit()
print(4)