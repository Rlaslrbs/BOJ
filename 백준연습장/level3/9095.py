T = int(input())

for i in range(T):
    
    num = int(input())
    dp = [0]*11
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    dp[4] = 7

    if num > 4:
        for i in range(5,num+1):
            dp[i] = dp[i-1] + dp[i-2] +dp[i-3]
        print(dp[num])


    else:
        print(dp[num])       





#dp[1] = 1
#dp[2] = 2  1+1, 2
#dp[3] = 4  1+1+1, 1+2, 2+1 , 3
#dp[4] = 7  1+1+1+1, 1+1+2 * 3, 1+3 * 2, 2+2 
#dp[5] = 13 1+1+1+1+1, 1+1+1+2 * 4, 1+2+2 * 3, 1+1+3 * 3, 2+3*2
#dp[6] = 24 1+1+1+1+1+1, 1+1+1+1+2 *5, 1+1+2+2 * 6,  1+1+1+3 *4, 1+2+3 * 6 3+3 1
#dp[7] = 44  1+1+1+1+1+1+1, 1+1+1+1+1+

# n>=4 
# dp[n] = dp[n-1]+dp[n-2]+dp[n-3]