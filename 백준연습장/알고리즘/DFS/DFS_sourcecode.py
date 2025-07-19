def dfs(graph, start):
    need_visited, visited = list(), list()

    need_visited.append(start)

    while need_visited:
        node = need_visited.pop()
        if node not in visited:
            visited.append(node)
            need_visited.extend(graph[node])

    return visited
