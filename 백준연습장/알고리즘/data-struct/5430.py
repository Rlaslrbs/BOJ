from collections import deque
import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    order = input().strip()
    n = int(input())
    arr_input = input().rstrip()
    if n == 0:
        arr = []
    else:
        arr = arr_input[1:-1].split(',')
    dq = deque(arr)

    error_flag = False
    reverse = False

    for cmd in order:
        if cmd == 'R':
            reverse = not reverse
        elif cmd == 'D':
            if dq:
                if not reverse:
                    dq.popleft()
                else:
                    dq.pop()
            else:
                print('error')
                error_flag = True
                break

    if not error_flag:
        if reverse:
            dq.reverse()
        print("[" + ",".join(dq) + "]")













