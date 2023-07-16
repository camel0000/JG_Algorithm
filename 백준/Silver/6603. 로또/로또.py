# 6603 : 로또

import sys
input = sys.stdin.readline
from itertools import combinations

while 1:
    A = list(map(int, input().split()))
    k = A[0]
    A.remove(k)
    
    if k == 0:
        exit()
    
    lottos = list(combinations(A, 6))
    
    for i in lottos:
        print(' '.join(map(str, i)))
    print()