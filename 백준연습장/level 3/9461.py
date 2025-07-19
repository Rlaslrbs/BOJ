



# 9  P(4) + P(9)  = P(10)
# 12 P(6) + P(10) = p(11)
# 16 P(7) + P(11) = P(12)
# 21 P(8) + P(12) = P(13)

# n > 9
# P(n) = P(n-1) + P(n-6)


t = int(input())
for _ in range(t):
    p=[0]*101
    p[1]=1
    p[2]=1
    p[3]=1
    p[4]=2
    p[5]=2
    p[6]=3
    p[7]=4
    p[8]=5
    p[9]=7
    num = int(input())
    if num > 9:
        for i in range(10,num+1):
            p[i] = p[i-1] + p[i-5]
        print(p[num])
    else:
        print(p[num])