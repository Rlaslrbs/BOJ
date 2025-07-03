
dp=[]

n = int(input())
sum_dp = [0] * n


dp = list(map(int, input().split()))

dp.sort()

sum_dp[0] = dp[0] 



for i in range(1, n):
    sum_dp[i] = dp[i] + sum_dp[i-1]


print(sum(sum_dp))





