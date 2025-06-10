
N, M = map(int,input().split())

tree = list(map(int,input().split()))


low = 0
high = max(tree)
while low <= high:
    mid = (low + high) // 2
    count = 0

    for i in tree:
        if i >= mid:
            count+=(i - mid)

    if count >= M:
        low = mid + 1
    else: 
        high = mid - 1

print(high)
