m , n = map(int,input().split())
data={}
for i in range(m):
    k,v = map(str,input().split())
    data[k] = v


for i in range(n):
    k = input()
    value = data.get(k)
    print(value)


    
