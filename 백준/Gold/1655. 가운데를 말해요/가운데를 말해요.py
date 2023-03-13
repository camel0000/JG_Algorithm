# 1655 : 가운데를 말해요

import sys
input = sys.stdin.readline
import heapq

N = int(input())

left_heap = []  # max heap
right_heap = [] # min heap

for _ in range(N):
    X = int(input())
    
    if len(left_heap) == len(right_heap):   # 왼쪽에서 중간값 구할 것으로, 항상 두 힙의 길이 같거나 왼쪽이 +1이어야 함
        heapq.heappush(left_heap, -X)
    else:
        heapq.heappush(right_heap, X)
        
    if right_heap and -left_heap[0] > right_heap[0]:    # 오른 힙이 비어있지 않고, 왼쪽 힙(max힙)의 루트가 오른쪽보다 크면 (오른쪽이 더 커야한다!)
        # 양 쪽 힙의 루트 교환(항상 오른쪽(min)이 더 커야, 총 개수가 짝수일 때, 출력 시 왼쪽의 작은 값을 출력할 수 있음)
        left_tmp = heapq.heappop(left_heap)
        right_tmp = heapq.heappop(right_heap)
        
        heapq.heappush(left_heap, -right_tmp)
        heapq.heappush(right_heap, -left_tmp)
    
    print(-left_heap[0])