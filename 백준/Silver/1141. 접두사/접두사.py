# 23-04-25
# 1141 : 접두사

import sys
input = sys.stdin.readline

N = int(input())
words = [input().rstrip() for _ in range(N)]
words.sort(key=len)

X = []

for i in range(N):
    check = 0
    for j in range(i + 1, N):
        if words[i] == words[j][:len(words[i])]:
            check = 1
            break

    if check == 0:
        X.append(words[i])

# print("=========")
# for i in range(len(X)):
    # print(''.join(map(str, X[i])))
print(len(X))