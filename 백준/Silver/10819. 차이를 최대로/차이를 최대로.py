# 10819 : 차이를 최대로

import sys
input = sys.stdin.readline

def recursion(li):      # 매개변수는 처음에는 빈 배열, 재귀가 일어나면서 배열 원소가 채워짐
    global rs           ### 전역 선언을 왜 해줘야 하는 지, 이해가 잘 안감 ㅠㅠ
    if len(li) == N:        # 모든 숫자에 대한 계산이 이루어지면(li 배열에 원소가 N개 모두 차면), 재귀 탈출
        total = 0
        for i in range(N - 1):      # 계산식
            total += abs(li[i] - li[i + 1])
        rs = max(rs, total)
        return
    
    for i in range(N):
        if not visited[i]:      # 계산이 안된 수 일 경우
            visited[i] = 1
            li.append(A[i])
            
            recursion(li)
            
            visited[i] = 0      # 한 번 계산식 만들었으면 방문 배열 초기화, li 배열도 pop으로 초기화
            li.pop()

N = int(input())
A = list(map(int, input().split()))

visited = [0] * N   # 이미 계산한 숫자 확인을 위한 배열
rs = 0

recursion([])   # 빈 배열을 매개변수로 하여, 순열을 만들 재귀함수 호출
print(rs)