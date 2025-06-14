N, C = map(int,input().split())
house = []
for i in range(N):
    house.append(int(input()))

house.sort()
# 1 2 4 8 9
low = 1
high = house[-1] - house[0]
while low <= high:
    mid = (low + high) // 2
    current = house[0]
    count = 1

    for i in range(1,len(house)):
        if house[i] >= current + mid :
            count += 1 
            current = house[i]
    if count >= C:
        low = mid + 1
        result = mid
    else:
        high = mid - 1

print(result)



    



