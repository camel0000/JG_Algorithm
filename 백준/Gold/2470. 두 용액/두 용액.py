# 2470 : 두 용액

import sys
input = sys.stdin.readline

N = int(input())
values = sorted(list(map(int, input().split())))    # 양수는 산성 / 음수는 알칼리성 !

tmp_sum = 2e9       # 두 용액 합의 절대값을 이용하여 0에 가장 가까운 두 수로 갱신하기 위한 임시 변수
start = 0
end = N - 1         # 용액 특성값들만 이용하여 비교하면 되므로, index 값을 start, end로 지정

while start < end:              # 같을 경우는 제외해야 함 / 0에 가장 가까운 값이 중복 적용될 수 있음
    _sum = values[start] + values[end]  # 새 용액의 진짜 특성값 / 일반적인 이분 탐색의 mid 역할을 대신해 줄 수도 있음

    if abs(_sum) < tmp_sum:     # 특성값을 0에 가까운 지 판단 위해 절대값화
        tmp_sum = abs(_sum)
        rs = (values[start], values[end])
    
    if _sum == 0: break
    elif _sum > 0: end -= 1
    else: start += 1
print(' '.join(map(str, rs)))