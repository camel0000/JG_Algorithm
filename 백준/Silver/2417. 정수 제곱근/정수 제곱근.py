# 2417 : 정수 제곱근

import sys
input = sys.stdin.readline


n = int(input())

start = 0
end = n

while start <= end:
    mid = (start + end) // 2
    
    if mid * mid < n:   # q^2 >= n인 가장 작은 음이 아닌 정수를 구하는 것이니,,
        start = mid + 1
    else:
        end = mid - 1

print(start)