# 23-05-23
# 옹알이 (2)

def solution(babbling):
    answer = 0
    
    for s in babbling:
        for b in ["aya", "ye", "woo", "ma"]:
            if b * 2 not in s:
                s = s.replace(b, ' ')
        if s.strip() == '':
            answer += 1    
    return answer

babbling = ["aya", "yee", "u", "maa"]
print(solution(babbling))
babbling = ["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]
print(solution(babbling))