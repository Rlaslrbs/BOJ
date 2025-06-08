n, m = map(int,input().split())

k = list(map(int,input().split()))
    
sum = 0
result = []


for i in range(n):
    for j in range(i+1,n):
        for u in range(j+1,n):
            sum = k[i]+k[j]+k[u]
            if sum > m:
                continue
            else:
                result.append(sum)
                
print(max(result))




