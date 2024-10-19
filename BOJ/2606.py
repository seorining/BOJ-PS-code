import sys

def dps(graph, start):
    count = []
    visited = set()
    
    def _dps(node):        
        visited.add(node)
        count.append(node)
        
        for vertex in graph[node]:
            if vertex not in visited:
                _dps(vertex)
    
    _dps(start)
    return count


computer_count = int(sys.stdin.readline().rstrip())
edge = int(sys.stdin.readline().rstrip())

graph = [[] for _ in range(computer_count+1)]

for i in range(edge):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    graph[x].append(y)
    graph[y].append(x)
    graph[x].sort()
    graph[y].sort()

print(len(dps(graph, 1))-1)