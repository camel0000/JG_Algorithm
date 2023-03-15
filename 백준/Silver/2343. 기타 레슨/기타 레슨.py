# 2343 : 기타 레슨

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lecs = list(map(int, input().split()))

total = sum(lecs)

start = 0
end = 1e9
rs = total

while start <= end:
    mid = (start + end) // 2
    
    if mid < max(lecs):
        start = mid + 1
        continue
    
    cnt = 1     # 블루레이 개수
    tmp = 0     # 갱신해줄 때 이용하는 블루레이의 길이
    
    for i in range(N):
        if tmp + lecs[i] <= mid:
            tmp += lecs[i]
        else:
            tmp = lecs[i]
            cnt += 1
    
    if cnt <= M:
        end = mid - 1
        rs = min(rs, mid)
    else:
        start = mid + 1

print(int(rs))