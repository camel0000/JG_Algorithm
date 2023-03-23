N, K = map(int, input().split())

arr = [int(input()) for _ in range(N)]
cnt = 0

for x in reversed(range(N)) :
    cnt += (K // arr[x])
    K = K % arr[x] 
        
print(cnt)