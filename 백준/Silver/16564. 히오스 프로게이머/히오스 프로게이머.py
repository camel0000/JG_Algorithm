# 16564 : 히오스 프로게이머

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
levels = []

for _ in range(N):
    levels.append(int(input()))
levels.sort()

start = levels[0]
end = levels[0] + K

rs = 0

while start <= end:
    mid = (start + end) // 2    # mid == 팀 목표 레벨 / 결국 mid를 출력해야 한다!
    
    tmp = sum(mid - i if i < mid else 0 for i in levels)
    
    if K == tmp:
        rs = mid
        break
    elif K > tmp:
        start = mid + 1
        rs = mid
    else:
        end = mid - 1
        
print(rs)