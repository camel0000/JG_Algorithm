# 2805_02 : 나무 자르기

def binarySearch(start, end):
    while start <= end:
        mid = (start + end) // 2
        target = sum(i - mid if i > mid else 0 for i in trees)
    
        if target >= M:
            start = mid + 1
        else:
            end = mid - 1
    
    return end

N, M = map(int, input().split())
trees = list(map(int, input().split()))

start = 0
end = max(trees)

print(binarySearch(start, end))