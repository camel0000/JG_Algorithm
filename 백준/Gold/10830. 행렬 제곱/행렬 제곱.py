# 10830 : 행렬 제곱

import sys
input = sys.stdin.readline

def multi(N, mat1, mat2):   # 행렬 곱하기
    result = [[0 for _ in range(N)] for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] += mat1[i][k] * mat2[k][j]
            result[i][j] %= 1000

    return result

def div(N, B, mat):         # 2분할하기
    if B == 1:
        return mat
    elif B == 2:
        return multi(N, mat, mat)
    else:
        tmp = div(N, B // 2, mat)
        
        if B % 2 == 0:
            return multi(N, tmp, tmp)
        else:
            return multi(N, multi(N, tmp, tmp), mat)


N, B = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

rs = div(N, B, A)

for i in rs:
    for j in i:
        print(j % 1000, end=' ')
    print()