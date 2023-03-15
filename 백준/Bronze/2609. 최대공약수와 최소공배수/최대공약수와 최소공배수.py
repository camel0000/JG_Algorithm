import sys
input = sys.stdin.readline

a, b = map(int, input().split())

if a <= b:
    for i in range(a, 0, -1):
        if a % i == 0 and b % i == 0:
            X = i
            break
    print(X)
    print(b * (a // X))
        
else:
    for i in range(b, 0, -1):
        if b % i == 0 and a % i == 0:
            X = i
            break
    print(X)
    print(a * (b // X))