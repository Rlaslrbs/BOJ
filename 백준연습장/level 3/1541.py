n = input().split('-')

num = []

for i in n:
    sum = 0
    temp = i.split("+")
    for j in temp:
        sum+=int(j)
    num.append(sum)


k = num[0]

for i in range(1,len(num)):
    k -=num[i]

print(k)