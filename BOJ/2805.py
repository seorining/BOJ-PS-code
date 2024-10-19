import sys
input = sys.stdin.readline

n, m = map(int, input().split())

tree_length = list(map(int, input().split()))
    
start = 0
end = max(tree_length)

while start <= end:
    height = (start + end) // 2
    
    tree_pruning = 0
    for i in tree_length:
        if i - height > 0:
            tree_pruning += i - height
    
    if tree_pruning >= m:
        start = height + 1
    else:
        end = height - 1
    
print(end)