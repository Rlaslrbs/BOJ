from collections import deque
n = int(input())
m = int(input())

net =[[] for _ in range(n+1)]
computer = [0] * (n+1)

for i in range(m):
    a , b = map(int, input().split())
    net[a].append(b)
    net[b].append(a)


def bfs():
    count = 0 
    q = deque()
    q.append(1)
    computer[1] = 1
    while q:
        cur = q.popleft()
        for index, value in enumerate(net[cur]):
            if computer[value] == 0:
                q.append(value)
                computer[value] = 1
                count+=1
    print(count)

bfs()
        





    






