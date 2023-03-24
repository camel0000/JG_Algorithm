import sys

input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())

    persons = []
    for _ in range(N):
        a, b = map(int, input().split())
        persons.append((a, b))
        
    persons.sort(key=lambda x : x[0])
    
    rs = [persons[0]]
    for i in range(1, N):
        if persons[i][1] < rs[-1][1]:
            rs.append(persons[i])
            
    print(len(rs))