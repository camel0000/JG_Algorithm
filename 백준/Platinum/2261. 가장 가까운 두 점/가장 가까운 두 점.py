# 2261 : 가장 가까운 두 점

import sys
input = sys.stdin.readline

n = int(input())
coord = []
for _ in range(n):
    x, y = map(int, input().split())
    coord.append((x, y))
    
coord.sort()

def compute_min_dist(start, end):
    min_dist = int(1e10)
    for i in range(start, end - 1):
        for j in range(i + 1, end):
            dist = (coord[i][0] - coord[j][0]) ** 2 + (coord[i][1] - coord[j][1]) ** 2
            min_dist = min(min_dist, dist)
    return min_dist

def find_min_dist(start, end):
    size = end - start
    if size < 3:
        return compute_min_dist(start, end)
    
    mid = (start + end) // 2
    
    left = find_min_dist(start, mid)
    right = find_min_dist(mid, end)
    
    min_dist = min(left, right)
    
    check_point = []
    divide_x = coord[mid][0]
    for i in range(start, end):
        if (coord[i][0] - divide_x) ** 2 <= min_dist:
            check_point.append(coord[i])
    check_point.sort(key=lambda x:x[1])
    
    for i in range(len(check_point)):
        now = check_point[i]
        for j in range(i + 1, len(check_point)):
            compare = check_point[j]
            if (compare[1] - now[1]) ** 2 >= min_dist:
                break
            dist = (now[0] - compare[0]) ** 2 + (now[1] - compare[1]) ** 2
            min_dist = min(min_dist, dist)
    
    return min_dist 

print(find_min_dist(0, n))