# 2630_02 : 색종이 만들기

import sys
input = sys.stdin.readline

N = int(input())
sq = [list(map(int, input().split())) for _ in range(N)]

rs = []

def divPaper(N, x, y):
    color = sq[x][y]
    
    for i in range(x, x + N):       # 이중 for문으로 모든 좌표 검사
        for j in range(y, y + N):   # 각 좌표에서 재귀를 통해 인접 좌표의 색이 같은지 판별
            if color != sq[i][j]:
                divPaper(N // 2, x, y)                          # 1사
                divPaper(N // 2, x, y + (N // 2))               # 2사
                divPaper(N // 2, x + (N // 2), y)               # 3사
                divPaper(N // 2, x + (N // 2), y + (N // 2))    # 4사
                return
            
    rs.append(color)    # color가 1이면 1 저장 / 2면 2 저장

divPaper(N, 0, 0)
print(rs.count(0))
print(rs.count(1))