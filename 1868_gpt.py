from collections import deque

# 트리에서 가장 먼 노드를 구하는 BFS
def bfs(start, n, adj):
    dist = [-1] * (n + 1)
    dist[start] = 0
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        for neighbor in adj[node]:
            if dist[neighbor] == -1:  # 아직 방문하지 않은 경우
                dist[neighbor] = dist[node] + 1
                queue.append(neighbor)
    
    # 가장 먼 노드를 반환
    farthest_node = dist.index(max(dist))
    max_distance = max(dist)
    return farthest_node, max_distance

def main():
    n = int(input())  # 방의 개수
    
    if n == 1:
        print(0)
        return
    
    # 인접 리스트로 트리 구성
    adj = [[] for _ in range(n + 1)]
    
    for _ in range(n - 1):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)
    
    # 1. 임의의 노드(1번)에서 가장 먼 노드를 찾음
    farthest_node, _ = bfs(1, n, adj)
    
    
    # 2. 그 노드에서 가장 먼 노드를 찾아 트리의 지름을 구함
    farthest_node, diameter = bfs(farthest_node, n, adj)
    
    # 트리의 지름은 구했으므로, 이 지름을 반으로 나눈 값을 최악의 질문 수로 사용
    print((diameter + 1) // 2)

if __name__ == "__main__":
    main()