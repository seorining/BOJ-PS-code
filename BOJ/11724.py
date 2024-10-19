import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for i in range(n+1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    graph[u].sort()
    graph[v].sort()
    
stack = []
visited = set()
count = 0

for i in range(1, n+1):
    if i in visited:
        continue
    
    stack.append(i)
    visited.add(i)
    while stack:
        node = stack.pop()
        
        for v in graph[node]:
            if not v in visited:
                visited.add(v)
                stack.append(v)
    count += 1
    
print(count)