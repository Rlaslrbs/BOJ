t = int(input())

for i in range(t):
    a,b = map(int, input().split())
    ans = 0
    while a*4 < b:
        a+=1
        ans += 1
    if a*3 > b:
        ans += 3*a - b
    print(ans)