# 1부터 시작 
# dp는 기억하면서 풀기다 

#10 <- 9 <- 3 <- 1

# 1-> 3 -> 9 -> 10

# 1 -> 3 -> 6 -> 7 
# 1 -> 2 - > 6 -> 7

"""
k = int(input())

dp = [1]

n = 0
while dp[0] != k :
    if  k - dp[0] > 3:
        dp[0] = dp[0] * 3
    elif k - dp[0] == 1 :
        dp[0] = dp[0] + 1
    else:
        dp[0] = dp[0] * 2
    n += 1
    

    
print(n)        

"""

n  = int(input())

dp = [0] * (n+1)
#n = 10
for i in range(2,n+1):
    dp[i] = dp[i-1] + 1
    if i % 2 == 0:
        dp[i] = min(dp[i//2]+1, dp[i])
    if i % 3 == 0 :
        dp[i] = min(dp[i//3]+1, dp[i])
    
print(dp[n])






    


