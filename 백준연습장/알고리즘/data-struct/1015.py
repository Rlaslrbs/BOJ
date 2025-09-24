"""
p[0] = 1
p[1] = 2
p[2] = 0


B[1] = A[0] = 2
B[2]= A[1] = 3
B[0]= A[2] = 1
A = [2,3,1]
B = [1,2,3]
"""
# p수열은 A수열의 각 숫자가 몇번째로 작은지?
import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
# a_sorted = a.sort() # None
a_sorted = sorted(a) # [1,2,3] 
 

p=[]

for i in a:
    p.append(a_sorted.index(i))
    a_sorted[a_sorted.index(i)] = -2

for i in range(n):
    print(str(p[i]), end=' ')

