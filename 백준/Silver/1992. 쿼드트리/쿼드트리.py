# 1992 : 쿼드트리

import sys
input = sys.stdin.readline

def quadTree(N, x, y):
    check = quad[x][y]
    
    for i in range(x, x + N):
        for j in range(y, y + N):
            if check != quad[i][j]:
                print('(', end='')
                quadTree(N // 2, x, y)
                quadTree(N // 2, x, y + N // 2)
                quadTree(N // 2, x + N // 2, y)
                quadTree(N // 2, x + N // 2, y + N // 2)
                print(')', end='')
                return
    
    if check == 0:  # 모두 0인 경우
        print('0', end='')
    else:
        print('1', end='')


N = int(input())
quad = [list(map(int, input().rstrip())) for _ in range(N)]

quadTree(N, 0, 0)