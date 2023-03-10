# 2164 : 카드2

import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
cards = deque()

for i in range(1, N + 1):
    cards.append(i)

while len(cards) != 1:
    cards.popleft()
    cards.rotate(-1)
    
print(cards[0])