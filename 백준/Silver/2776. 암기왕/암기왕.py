# 2776 : 암기왕

import sys
input = sys.stdin.readline

def binarySearch(start, end, target):
    check = 0
    
    while start <= end:
        mid = (start + end) // 2
        
        if target == note1[mid]:
            check = 1
            break
        elif target < note1[mid]:
            end = mid - 1
        else:
            start = mid + 1
            
    if check == 1:
        return 1
    else:
        return 0


for _ in range(int(input())):       # 테스트 개수 T
    N = int(input())
    note1 = sorted(list(map(int, input().split())))
    
    M = int(input())
    note2 = list(map(int, input().split()))
    
    for n in note2:
        print(binarySearch(0, len(note1) - 1, n))