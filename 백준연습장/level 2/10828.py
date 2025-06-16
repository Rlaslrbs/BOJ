from collections import deque
import sys

input = sys.stdin.readline


n = int(input())
stack = deque()
for order in range(n):
    order = input()

    
    if order.startswith('push'): #push
        num = int(order.split()[1])
        stack.append(num)

    if order.startswith('pop'): #pop
        if len(stack) >= 1:
            temp = stack[-1]
            stack.pop()
            print(temp)
        else:
            print(-1)

    if order.startswith('size'): #size
        print(len(stack))
    
    if order.startswith('empty'): #empty
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    if order.startswith('top'): #top
        if len(stack) >= 1:
            print(stack[-1])
        else:
            print(-1)
