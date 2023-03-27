import sys
input = sys.stdin.readline

N, K = map(int, input().split())
order = list(map(int, input().split()))

tab = []
plug_out = 0

for i in range(K):
    if order[i] in tab:
        continue
    if len(tab) < N:
        tab.append(order[i])
    else:
        max_idx, max_val = -1, -1
        for j in range(N):
            if tab[j] not in order[i+1:]:
                max_idx = j
                break
            if order[i+1:].index(tab[j]) > max_val:
                max_idx = j
                max_val = order[i+1:].index(tab[j])
        tab[max_idx] = order[i]
        plug_out += 1

print(plug_out)