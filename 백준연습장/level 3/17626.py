
import math
n = int(input())
dp = [0] *(n+1)
dp[1]=1

for i in range(2,n+1):
    result = 4
    for j in range(1,int(math.sqrt(i))+1):
        result = min(result, dp[i-(j**2)])
    dp[i] = result + 1
print(dp[n])


