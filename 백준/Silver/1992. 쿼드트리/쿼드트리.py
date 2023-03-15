# 1992 : 쿼드트리

import sys
input = sys.stdin.readline

N = int(input())
quad = [list(map(int, input().strip())) for _ in range(N)]

def div_paper(N, x, y):
    number = quad[x][y]
    
    for i in range(x, x + N):
        for j in range(y, y + N):
            if number != quad[i][j]:    # 하나라도 다르면
                print('(', end='')
                
                div_paper(N // 2, x, y)
                div_paper(N // 2, x, y + N // 2)
                div_paper(N // 2, x + N // 2, y)
                div_paper(N // 2, x + N // 2, y + N // 2)
            
                print(')', end='')
                return
    if number == 0: # 모두 0
        print('0', end='')
        return
    else:
        print('1', end='')
        return

div_paper(N, 0, 0)