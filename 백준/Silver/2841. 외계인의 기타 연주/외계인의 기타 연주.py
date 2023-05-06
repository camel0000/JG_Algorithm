# 23-05-06
# 2841 : 외계인의 기타 연주

import sys
input = sys.stdin.readline

N, P = map(int, input().split())
mel = []
for _ in range(N):
    s_num, p_num = map(int, input().split())
    mel.append([s_num, p_num])
# print(mel)

finger = 0
stacks = [[], [], [], [], [], [], []]   # 스택 6개 + 1

for i in range(N):
    # print(stacks, finger)
    s_num, p_num = mel[i]
    breaker = 0

    if not stacks[s_num]:   # 해당 줄의 stack 비어있으면
        stacks[s_num].append(p_num)
        finger += 1
        continue
    
    if stacks[s_num][-1] < p_num:   # 현재 누를 프렛이 더 높으면
        stacks[s_num].append(p_num)
        finger += 1
    elif stacks[s_num][-1] > p_num: # 현재 누를 프렛보다 더 낮으면
        for j in range(len(stacks[s_num])):
            if breaker == 0:
                if stacks[s_num][j] == p_num:
                    tmp_j = j
                    breaker = 1
                    continue
            if breaker == 1:
                stacks[s_num].pop()
                finger += 1
            
        
        if breaker == 1:
            continue
        
        while stacks[s_num][-1] > p_num:
            stacks[s_num].pop()
            finger += 1
            if len(stacks[s_num]) == 0:
                break
        
        if not stacks[s_num]:
            stacks[s_num].append(p_num)
            finger += 1
            continue
        if stacks[s_num][-1] == p_num:
            continue
        stacks[s_num].append(p_num)
        finger += 1
    else:                           # 현재 누를 프렛과 같으면
        continue
# print('last', stacks)
print(finger)