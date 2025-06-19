from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
order = deque()

for i in range(n):
    a = input()

    if a.startswith('push'):
        num = int(a.split()[1])
        order.append(num)

    elif a.startswith('pop'):
        if len(order) == 0:
            print(-1)
        else:
            print(order[0])
            order.popleft()

    elif a.startswith('size'):
        print(len(order))

    elif a.startswith('empty'):
        if len(order) == 0:
            print(1)
        else:
            print(0)

    elif a.startswith('front'):
        if len(order) == 0:
            print(-1)
        else:
            print(order[0])
    elif a.startswith('back'):
        if len(order) == 0:
            print(-1)
        else:
            print(order[-1])

