n, k = map(int, input().split())

cash=[]

for i in range(n):
    cash.append(int(input()))

cash = list(reversed(cash))
count = 0
for won in cash:
    if k == 0:
        break
    count = count + (k // won)
    k = k % won

print(count)

