"""
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

n = int(input())


count = 0
reverse_str = ""
for i in str(factorial(n)):
    reverse_str = i + reverse_str

for i in reverse_str:

    i = int(i)
    if i == 0:
        count += 1
    else:
        print(count)
        break
 """  
n = int(input())
i = 5
count = 0 
while n >= i:
    if n // i != 0:
        count +=(n//i)
        i*=5

print(count)
    
