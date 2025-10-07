main = ['***', '* *', '***']

N = int(input())


def star(n=3,arr=main):
    if n == N:
        return arr
    
    temp = []

    for i in range(n): #상단
        temp.append(arr[i]*3)
    for i in range(n): #중단
        temp.append(arr[i]+" "*n+arr[i]) 
    for i in range(n):
        temp.append(arr[i]*3)

    return star(n*3, temp)

ans = star(3, main)

for line in ans:
    print(line)