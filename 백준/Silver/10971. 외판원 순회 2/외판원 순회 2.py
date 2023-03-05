# 10971 : 외판원 순회 2

import sys
input = sys.stdin.readline

def dfs(start, now, value, cnt):
    global rs
    
    if cnt == N:
        if W[now][start]:
            value += W[now][start]      # 마지막 도시 -> 출발 도시 비용 누적 추가
            
            if rs > value:
                rs = value
            
        return
    
    if value > rs:
        return
    
    for i in range(N):
        if not visited[i] and W[now][i]:    # 방문한 도시 아니고(visited[i] == 0이고), 길이 없는 다음 도시(혹은 현재 위치 도시)가 아니라면
            visited[i] = 1
            
            dfs(start, i, value + W[now][i], cnt + 1)   # value 파라미터에 값 누적, cnt 파라미터로 후에 재귀 탈출 조건으로 이용
            
            visited[i] = 0

N = int(input())
W = [list(map(int, input().split())) for _ in range(N)]

visited = [0] * N       # 도시 수 만큼 방문 기록 배열 범위 초기화

rs = sys.maxsize        # 결과값을 범위 내 최대치로 설정하여 아아아아주 많은 경로(비용)가 있더라도 최소 비용 산출 시 오작동하지 않도록 함

for i in range(N):      # 반복문으로 출발 도시 지정하여 dfs() 함수 호출
    visited[i] = 1
    dfs(i, i, 0, 1)     # 현재 위치는 출발 도시
    visited[i] = 0
    
print(rs)