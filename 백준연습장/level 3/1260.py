from collections import deque

n, m, v = map(int, input().split())

grp = [[] for _ in range(n+1)]

for i in range(m):
    a,b = map(int, input().split())
    grp[a].append(b)
    grp[b].append(a)

for i in range(1,n+1):
    grp[i].sort()

def dfs(start):
    visited = []

    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            if grp[node]:
                stack.extend(grp[node][::-1])

    return visited

def bfs(start):
    visited= [False] * (n+1)
    queue = deque([start])
    visited[start]= True

    ans=[]

    while queue:
        node = queue.popleft()
        ans.append(node)
        for i in grp[node]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    return ans


print(*dfs(v))
print(*bfs(v))