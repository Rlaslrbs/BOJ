
import math

m , n = map(int,input().split())

ans_n = []
ans=[]


array_n=[True] * (n +1)
array_n[0] = False # 0은 소수가 아님
array_n[1] = False # 1은 소수가 아님
for i in range(2,int(math.sqrt(n))+1): #n
     if array_n[i]: # 만약 i가 소수라면
        for j in range(i * i, n+1, i):
            array_n[j] = False


for i in range(n+1):
      if array_n[i]:
           ans_n.append(i) 


ans = [x for x in ans_n if x >= m]

for i in ans:
     print(i)

   



