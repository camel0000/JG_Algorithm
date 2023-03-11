# 2110 : 공유기 설치

import sys
input = sys.stdin.readline

def binarySearch(start, end):
    while start <= end:
        mid = (start + end) // 2    # mid == 출력 조건인, 가장 인접한 두 공유기 사이의 최대 거리
        cnt = 1
        
        installed = X[0]    # 직전 설치 위치 (여기서는 첫 위치이고, 리스트 X 중 첫 좌표일 수 밖에 없음)
        
        for i in range(1, len(X)):    # 범위는 인덱스로
            if X[i] - installed >= mid:  # mid는 공유기 사이의 최대 거리 기준으로, 이 보다 두 공유기 사이의 거리가 넓으면 i 좌표에 공유기 설치
                cnt += 1
                installed = X[i]        # 설치 위치 갱신
               
        # 위 과정을 거치며, cnt 값이 설정됨 ==> cnt == '설정된 mid 값'을 '두 공유기 사이 거리의 최대 격차'로 했을 때의 공유기 설치 가능 개수 
        
        if cnt >= C:            # 설치가 가능한 최대 개수(cnt)가 공유기의 개수(C)보다 크면, 
            rs = mid            # 출력할 결과값은 위에서 두 공유기 사이에 가질 수 있는 최대 거리인 mid
            start = mid + 1     # 범위를 뒷 절반 부분으로 좁혀줌 (최대 개수를 줄여줌)
        else:
            end = mid - 1       # 범위를 앞 절반 부분으로 좁혀줌 (최대 개수를 줄여줌)
    
    return rs
           
            
N, C = map(int, input().split())
X = []

for _ in range(N):
    X.append(int(input()))
X.sort()

start = 1           # 두 좌표 사이 거리의 최소값
end = X[-1] - X[0]  # 두 좌표 사이 거리의 최대값

print(binarySearch(start, end))