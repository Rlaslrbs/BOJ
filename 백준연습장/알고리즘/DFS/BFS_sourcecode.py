from collections import deque

def bfs(graph, start):
    visited= [False] * 9
    queue = deque([start])
    #현재 노드를 방문 처리 
    visited[start] = True
    #큐가 빌 때까지 반복
    while queue:
        #큐에서 하나의 원소를 뽑아 출력하기 
        v = queue.popleft()
        print(v, end='')
        #아직 방문하지 않은 인접한 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph = [
    [],          # Node 0 has no neighbors (or is unused, depending on your graph's indexing)
    [2, 3, 8],   # Node 1 is connected to nodes 2, 3, and 8
    [1, 7],      # Node 2 is connected to nodes 1 and 7
    [1, 4, 5],   # Node 3 is connected to nodes 1, 4, and 5
    [3, 5],      # Node 4 is connected to nodes 3 and 5
    [3, 4],      # Node 5 is connected to nodes 3 and 4
    [7],         # Node 6 is connected to node 7
    [2, 6, 8],   # Node 7 is connected to nodes 2, 6, and 8
    [1, 7]       # Node 8 is connected to nodes 1 and 7
]