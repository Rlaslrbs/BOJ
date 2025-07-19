"""
n , m = map(int, input().split())
num = list(map(int,input().split()))

for _ in range(m):
    sum = 0
    a,b = map(int,input().split())
    for i in range(a-1,b,1):
        sum += int(num[i])
    print(sum)
"""

n , m = map(int, input().split())
num = list(map(int,input().split()))

prefixSum = [0] * (n+1)


for i in range(1,n+1):
    prefixSum[i] = prefixSum[i-1] + num[i-1]

for _ in range(m):
    Partsum = 0
    a,b = map(int,input().split())
    Partsum = prefixSum[b] - prefixSum[a-1]
    print(Partsum)



# 5 4 3 2 1
# 5 9 12 14 15