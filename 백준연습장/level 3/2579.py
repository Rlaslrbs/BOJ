n = int(input())
stair=[0] * 301

for i in range(1,n+1):
    stair[i] = int(input())


dp = [0] *301
dp[1] = stair[1]
dp[2] = stair[1] + stair[2]
dp[3] = max(stair[1] + stair[3], stair[2] + stair[3])

for i in range(4, n+1):
    dp[i] = max(stair[i] + stair[i-1] + dp[i-3], stair[i] + dp[i-2])



print(dp[n])


#dp(n) = max(직전칸에서 올라온 경우의 최댓값, 전전칸에서 올라온 경우의 최댓값 )
#dp(n) = max(stair(n) + stair(n-1) + dp(n-3), stair(n) + dp(n-2))


