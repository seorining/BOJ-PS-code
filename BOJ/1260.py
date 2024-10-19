from collections import deque
import sys
input = sys.stdin.readline

def dps(graph, start):
    res = []
    visited = set()
    
    def _dps(node):
        visited.add(node)
        res.append(node)
        
        for vertex in graph[node]:
            if vertex not in visited:
                _dps(vertex)
    _dps(start)
    
    return res

def bps(graph, start):
    res = []
    queue = deque([start])
    visited = set([start])
    
    while queue:
        node = queue.popleft()
        res.append(node)
        
        for vertex in graph[node]:
            if vertex not in visited:
                queue.append(vertex)
                visited.add(vertex)
    return res

n, m, start = map(int, input().split())

graph = [[] for _ in range(n+1)]

for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in graph:
    i.sort()

print(*dps(graph, start), sep=' ')
print(*bps(graph, start), sep=' ')