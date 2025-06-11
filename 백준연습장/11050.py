def factorial(n):
    res = 1
    for i in range(1,i+1):
        res *= i
        return res
        
N, K = map(int,input().split())

result_top = factorial(N)
result_bottom = factorial((N-K)) * factorial(K)

print(int(result_top / result_bottom))
