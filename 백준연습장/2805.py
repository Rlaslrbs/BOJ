N,M = map(int,input().split())

tree = list(map(int,input().split()))

result = []
low = 0
high = max(tree)
while low <= high:
    count = 0
    mid = (low + high) // 2
    for i in tree:
        if i > mid:
            g = i - mid

            count+=g
    if count >= M:
        result = mid
        low = mid + 1
    else: 
        high = mid -1

print(result)
