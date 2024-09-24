graph1 = {1: [2, 3, 5], 2: [1, 3], 3: [1, 2, 4], 4: [3, 5], 5: [1, 4]} #무방향 그래프
graph2 = {1: [2, 3], 2: [3], 3: [4], 4: [], 5: [1, 4]}                 #방향 그래프

def bfs(graph, node):
    res = []
    queue = [node]
    visited = set()
    
    while queue:
        u = queue.pop(0)
        res.append(u)
        for v in graph[u]:
            if v not in visited:
                visited.add(v)
                queue.append(v)
    return res

print("무방향 그래프의 너비 우선 탐색")
print("==========================")
print("노드 1에서 시작: ", bfs(graph1, 1))
print("노드 2에서 시작: ", bfs(graph1, 2))
print()
print("방향 그래프의 너비 우선 탐색")
print("========================")
print("노드 1에서 시작: ", bfs(graph2, 1))
print("노드 2에서 시작: ", bfs(graph2, 2))

from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] * 9

bfs(graph, 1, visited)
print()