
N, k  = int(input()), int(input())
low = 1
high = k

while low <= high:
    mid = (low + high) // 2

    temp = 0
    for i in range(1,N+1):
        temp += min(mid//i , N)

    if temp >= k:
        ans = mid
        high = mid - 1

    else:
        low = mid + 1

print(ans)   

