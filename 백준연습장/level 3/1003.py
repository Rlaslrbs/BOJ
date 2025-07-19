"""

import sys

input = sys.stdin.readline

def fibonacci(n):
    if n == 0:
        return (1,0)
    elif n == 1:
        return  (0,1)
    else: 
        count0_n_minus_1, count1_n_minus_1 = fibonacci(n - 1)
        count0_n_minus_2, count1_n_minus_2 = fibonacci(n - 2)

        total_0 = count0_n_minus_1 + count0_n_minus_2
        total_1 = count1_n_minus_1 + count1_n_minus_2


        return (total_0, total_1)
    
t = int(input())

for i in range(t):
    ans = list(fibonacci(int(input())))
    for i in ans:
        print(i)


"""
T = int(input())
zero = [1,0,1]
one  = [0,1,1]

def solve(n):
    if len(zero) <= n :
        for i in range(len(zero),n+1):
            zero.append(zero[i-1]+zero[i-2])
            one.append(one[i-1]+one[i-2])
    print(zero[n],one[n])


for i in range(T):
    a = int(input())
    solve(a)

