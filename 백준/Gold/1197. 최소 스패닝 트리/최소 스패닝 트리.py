# 1197 : 최소 스패닝 트리
# 크루스칼 기법

import sys
input = sys.stdin.readline

V, E = map(int, input().split())

vertices = [i for i in range(V + 1)]
edges = []

for _ in range(E):
    edges.append(list(map(int, input().split())))

edges.sort(key=lambda x: x[2])  # 각 정보 리스트의 3번째 원소인 가중치 기준으로 오름차순 정렬

def find(x):
    if x != vertices[x]:
        vertices[x] = find(vertices[x])
    return vertices[x]

rs = 0

for start, end, weight in edges:
    start_root = find(start)
    end_root = find(end)
    
    if start_root != end_root:
        if start_root > end_root:
            vertices[start_root] = end_root
        else:
            vertices[end_root] = start_root
        
        rs += weight

print(rs)