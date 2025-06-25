import sys
input = sys.stdin.readline

n ,m = map(int,input().split())
data={}
n_data={}
for i in range(1,n+1):
    name = input().strip()
    data[i] = name
    n_data[name] = i

for j in range(m):
    a = input().strip()
    if a[0].isalpha() == True: #문자열 판별    
        print(n_data[a])
    else:
        a=int(a)
        value = data[a]
        print(value)
