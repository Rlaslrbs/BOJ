import sys
input = sys.stdin.readline
n = int(input())
stack = []
order = []
count = 1
temp = True

for i in range(n):
    num = int(input())
    while num >= count:
        stack.append(count)
        order.append('+')
        count+=1

    if stack[-1] == num:
        stack.pop()
        order.append("-")
    else:
        temp = False


if temp == True:
    for i in order:
        print(i)

else:
    print("NO")


"""
1234 ++++
12  43 --
1256  43 ++
125 436 -
12578 436 ++
"""
# [1,2,3,4] 같이 마지막 스택 수와 수열의 첫째 수가 같지 않으면 x




