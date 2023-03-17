# 5639 : 이진 검색 트리

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

numbs = []

while 1:
    try:
        numbs.append(int(input()))
    except:
        break
    
def postorder(left, right):
    if left > right:
        return
    mid = right + 1
    
    for i in range(left + 1, right + 1):
        if numbs[left] < numbs[i]:
            mid = i
            break
            
    postorder(left + 1, mid - 1)    # 왼쪽 확인
    postorder(mid, right)           # 오른쪽 확인
    print(numbs[left])
        
postorder(0, len(numbs) - 1)