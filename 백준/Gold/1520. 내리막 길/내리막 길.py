import sys
input = sys.stdin.readline

M, N = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(M)]
dp = [[-1] * N for _ in range(M)]   # 메모이제이션을 위한 배열, -1로 초기화

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(a, b):
    if a == M-1 and b == N-1:
        return 1   # 경로가 가능한 경우 1 반환
    
    if dp[a][b] != -1:   # 이미 방문한 적이 있다면, 저장된 값을 반환
        return dp[a][b]
    
    dp[a][b] = 0   # 메모이제이션을 위해 0으로 초기화
    
    for k in range(4):
        nx, ny = a + dx[k], b + dy[k]
                
        if 0 <= nx < M and 0 <= ny < N and maps[nx][ny] < maps[a][b]:
            dp[a][b] += dfs(nx, ny)
    
    return dp[a][b]   # 경로의 수 반환

print(dfs(0, 0))