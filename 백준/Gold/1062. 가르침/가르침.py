# 1062 : 가르침

import sys
input = sys.stdin.readline
from itertools import combinations

n, k = map(int, input().rstrip().split())
words = [set(input().rstrip()).difference('a', 'c', 'i', 't', 'n') for _ in range(n)]

if k < 5:
    print(0)
    exit()

letters = {chr(i + 97): i for i in range(26)}
ids = [i for i in range(26) if chr(i + 97) not in ['a', 'c', 'i', 't', 'n']]

k -= 5
res = 0
for comb in combinations(ids, k):
    mask = 0
    for move in comb:
        mask |= 1 << move

    cnt = 0
    for word in words:
        wordbit = 0
        for char in word:
            wordbit |= 1 << letters[char]
        if mask | wordbit == mask:
            cnt += 1
    res = max(cnt, res)

print(res)