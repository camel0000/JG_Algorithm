import sys
input = sys.stdin.readline

M, N, L = map(int, input().split())
X = sorted(list(map(int, input().split())))

rs = 0

lo = []
for _ in range(N):
    a, b = map(int, input().split())
    lo.append((a, b))
    
for i in lo:
    check = 0
    
    for j in X:
        if abs(j - i[0]) + i[1] <= L:
            rs += 1
            check = 1
            
        if check == 1:
            break
print(rs)