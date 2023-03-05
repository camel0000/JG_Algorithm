# 9663 : N-Queen

import sys
input = sys.stdin.readline

def adjacent(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == x - i:
            return False
    return True

def dfs(x):     # 행 값을 매개변수로
    global rs
    
    if x == N:
        rs += 1
    else:
        for i in range(N):
            row[x] = i          # 해당 행의 열들을 0~N까지 확인, 반복문 통해 퀸을 놓을 수 있는 곳 찾기
            
            if adjacent(x):     # 해당 행에 퀸 놓을 수 있는 지 확인 / True 반환이면 백트래킹 안하고 다음 행으로 진행
                dfs(x + 1)


N = int(input())

row = [0] * N   # 각 행의 열들 방문 검사용 배열
rs = 0          # 결과값

dfs(0)          # 0행부터 확인
print(rs)