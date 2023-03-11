# 10815 : 숫자 카드

import sys
input = sys.stdin.readline

def binarySearch(start, end, target):
    check = 0
    
    while start <= end:
        mid = (start + end) // 2
        
        if target == cards[mid]:
            check = 1
            break
        elif target > cards[mid]:
            start = mid + 1
        else:
            end = mid - 1
            
    if check == 1:
        return 1
    else:
        return 0

N = int(input())
cards = sorted(list(map(int, input().split())))
M = int(input())
_list = list(map(int, input().split()))

for i in _list:
    print(binarySearch(0, len(cards) - 1, i))