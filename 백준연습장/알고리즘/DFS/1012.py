import sys
sys.setrecursionlimit(10**6)


def dfs(x,y):
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0<= nx < m) and (0<= ny < n) and field[ny][nx] == 1:
            field[ny][nx] = 2
            dfs(nx,ny)






T = int(input())

for _ in range(T):
    m,n,k = map(int,input().split())
    field = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        x, y = map(int,input().split())
        field[y][x] = 1

    count = 0
    for a in range(m):
        for b in range(n):
            if field[b][a] == 1:
                dfs(a,b)
                count+=1

    print(count)






