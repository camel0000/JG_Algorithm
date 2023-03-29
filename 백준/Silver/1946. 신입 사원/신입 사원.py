# 1946_03 : 신입 사원

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    persons = sorted([tuple(map(int, input().split())) for _ in range(N)], key=lambda x : x[0])

    rs = [persons[0]]

    for person in persons:
        if person[1] < rs[-1][1]:
            rs.append(person)

    print(len(rs))