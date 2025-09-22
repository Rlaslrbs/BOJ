
n , k = map(int,input().split())


queue = [] #환형 큐 
result = [] #정답

for i in range(1,n+1):
    queue.append(i)

count = 0

num = 0
for i in range(n):
    num += k-1
    if num >= len(queue):
        num = num%len(queue)

    result.append(str(queue.pop(num)))


print("<",", ".join(result)[:],">", sep='')






'''
1 2 3 4 5 6 7 < >

1 2 4 5 6 7 <3>

1 2 4 5 7 <3,6>



'''




