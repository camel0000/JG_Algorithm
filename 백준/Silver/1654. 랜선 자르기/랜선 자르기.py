# 1654 : 랜선 자르기

import sys
input = sys.stdin.readline

def binarySearch(start, end):
    while start <= end:
        mid = (start + end) // 2
        cnt = 0     # target인 셈이다.
        
        for i in LANs:
            cnt += (i // mid)
        
        if cnt >= N:
            start = mid + 1
        else:
            end = mid - 1

    return end

K, N = map(int, input().split()) # K는 이미 가지고 있는 랜선 개수 / N은 필요한 랜선 개수
LANs = []

for _ in range(K):
    LANs.append(int(input()))
    
print(binarySearch(1, max(LANs)))