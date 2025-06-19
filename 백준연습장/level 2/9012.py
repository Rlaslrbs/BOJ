import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    a = input()
    stack=[]
    
    for k in a:
        if k == '(':
            stack.append(k)

        elif k == ')' :
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(k)

    if len(stack) == 0:
        print('YES')
    else:
        print('NO')
            
        
