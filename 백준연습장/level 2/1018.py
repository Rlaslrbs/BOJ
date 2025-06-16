n , m = map(int,input().split())
data=[]
change=[]
for i in range(n):
    data.append(input())

for a in range(n-7): # 세로
    for b in range(m-7): # 가로
        std_w = 0
        std_b = 0
        for i in range(a,a+8):
            for j in range(b,b+8):
                if (i+j) % 2 == 0: #짝수
                    if data[i][j] != 'W':
                        std_w +=1
                    if data[i][j] != 'B':
                        std_b +=1

                else:
                    if data[i][j] == 'W':
                        std_w+=1
                    if data[i][j] == 'B':
                        std_b += 1
        change.append(min(std_w, std_b))

print(min(change))
            






    #i+j가 짝수이면 시작점의 색과 같음
    #홀수이면 시작점의 색깔과 다름 


