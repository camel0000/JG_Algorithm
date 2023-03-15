import sys
input = sys.stdin.readline

N = int(input())
requests = sorted(list(map(int, input().split())))
budget = int(input())

start = 0
end = max(requests)

if sum(requests) <= budget:
    print(end)
else:
    while start <= end:
        mid = (start + end) // 2

        total = 0
        for req in requests:
            if req < mid:
                total += req
            else:
                total += mid * (N - requests.index(req))
                break

        if total > budget:
            end = mid - 1
        else:
            start = mid + 1
            answer = mid

    print(answer)