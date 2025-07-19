import sys
input = sys.stdin.readline
S = set()
m = int(input())

for i in range(m):
    order = list(input().split())
    o = order[0]


    if o == 'add':
        S.add(int(order[1]))

    elif o == 'remove':
        S.discard(int(order[1]))
    
    elif o == 'check':
        if int(order[1]) in S:
            print(1)
        else:
            print(0)
    
    elif o == 'toggle':
        if int(order[1]) in S:
            S.discard(int(order[1]))
        else:
            S.add(int(order[1]))
    
    elif o == 'all':
        S = set([i for i in range(1,21)])
    
    else:
        S = set()

