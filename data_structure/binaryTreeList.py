"""
인덱스  0	1	2	3	4	5	6	 7
값     A   B   C   D   E   F  None  G

루트 A의 인덱스는 0
A의 왼쪽 자식인 B의 인덱스: 2 × 0 + 1 = 1
A의 오른쪽 자식인 C의 인덱스: 2 × 0 + 2 = 2
B의 인덱스는 1
B의 왼쪽 자식인 D의 인덱스: 2 × 1 + 1 = 3
B의 오른쪽 자식인 E의 인덱스: 2 × 1 + 2 = 4
C의 인덱스는 2
C의 왼쪽 자식인 F의 인덱스: 2 × 2 + 1 = 5
D의 인덱스는 3
D의 왼쪽 자식인 G의 인덱스: 2 × 3 + 1 = 7

부모 노드의 인덱스가 n일 때, 
왼쪽 자식 노드의 인덱스는 (2 × n + 1)이며 오른쪽 자식 노드의 인덱스는 (2 × n + 2)이다. 
이진트리는 자식 노드가 2개 이하이므로 위와 같은 규칙에 따라 배열에 넣을 수 있다.

반대로 자식 노드의 부모 노드를 찾으려면, 
자식 노드의 인덱스에서 1을 뺀 후에 2로 나눈 몫만 취하면 된다. 
예를 들어 D의 부모 노드의 인덱스를 찾으면 (3 - 1) // 2 = 1이다.

인덱스 0은 비워두고, 인덱스 1부터 자료를 넣어 트리를 구성하기도 한다. 
그렇게 하면 왼쪽 자식 노드의 인덱스는 (2 × n), 오른쪽 자식 노드의 인덱스는 ( 2 × n + 1)이다.
그럼 부모 노드의 인덱스는 자식 노드의 인덱스를 2로 나눈 몫만 취하면 된다.
"""

#Find child node
tree = ["A", "B", "C", "D", "E", "F", None, "G"]

i = 0
n = len(tree)
while i < n:
    if tree[i]:
        print(f"Parent: {tree[i]}", end = ", ")
        left = 2 * i + 1
        right = left + 1
        if left < n and tree[left] is not None:
            print(f"Left: {tree[left]}", end = ", ")
        if right < n and tree[right] is not None:
            print(f"Right: {tree[right]}", end = " ")
        print()
    i += 1
    
#Find Parent node
i = n-1
while i > 0:
    if tree[i]:
        print(f"Parent of {tree[i]} -> {tree[(i-1)//2]}")
    i -= 1
print()

################################################################
tree = ["A", "B", "C", "D", "E", "F", None, "G"]
################################################################
##재귀 순회 함수 만들기

#전위 순회 함수 만들기 VLR (재귀)
def preorder(tree):
    def _preorder(i = 0):
        if i >= len(tree) or tree[i] is None:
            return
        res.append(tree[i])
        _preorder(2 * i + 1)
        _preorder(2 * i + 2)
    
    res = []
    _preorder()
    return res
        
print("Preorder : ", end='')
print(preorder(tree))


#중위 순회 함수 만들기 LVR (재귀)
def inorder(tree):
    def _inorder(i = 0):
        if i >= len(tree) or tree[i] is None:
            return
        _inorder(2 * i + 1)
        res.append(tree[i])
        _inorder(2 * i + 2)
    
    res = []
    _inorder()
    return res

print("Inorder : ", end='')
print(inorder(tree))


#후위 순회 함수 만들기 LRV (재귀)
def postorder(tree):
    def _postorder(i=0):
        if i >= len(tree) or tree[i] is None:
            return
        _postorder(2 * i + 1)
        _postorder(2 * i + 2)
        res.append(tree[i])
    
    res = []
    _postorder()
    return res

print("Postorder : ", end='')
print(postorder(tree))

################################################################
tree = ["A", "B", "C", "D", "E", "F", None, "G"]
################################################################
## 스택으로 순회 함수 만들기

#전위 순회 함수 만들기 VLR (스택)
def preorder(tree):
    if not tree:
        return []
    res, stack = [], [0]
    
    while stack:
        index = stack.pop()
        res.append(tree[index])
        index = 2 * index + 2
        if index < len(tree) and tree[index] is not None:
            stack.append(index)
        index -= 1
        if index < len(tree) and tree[index] is not None:
            stack.append(index)
    return res

print(preorder(tree))

#중위 순회 함수 만들기 LVR (스택)
def inorder(tree):
    if not tree:
        return []
    index = 0
    res, stack = [], []
    
    while True:
        if index < len(tree) and tree[index] is not None:
            stack.append(index)
            index = 2 * index + 1
        elif stack:
            index = stack.pop()
            res.append(tree[index])
            index = 2 * index + 2
        else:
            break
    return res

print(inorder(tree))


#후위 순회 함수 만들기 LRV (스택)
def postorder(tree):
    if not tree:
        return []
    res, stack = [], [0]
    visit_order = []
    
    while stack:
        index = stack.pop()
        visit_order.append(index)
        index = 2 * index + 1
        if index < len(tree) and tree[index] is not None:
            stack.append(index)
        index += 1
        if index < len(tree) and tree[index] is not None:
            stack.append(index)
    
    while visit_order:
        index = visit_order.pop()
        res.append(tree[index])
    return res

### 전위 순회를 활용해 구현 ##
# 순회 (부모 - 오른쪽 - 왼쪽) 후 그 결과를 뒤집으면 왼쪽 - 오른쪽 - 부모
def postorder(tree):
    if not tree:
        return []
    res, stack = [], [0]
    
    while stack:
        index = stack.pop()
        res.append(tree[index])
        index = 2 * index + 1
        if index < len(tree) and tree[index] is not None:
            stack.append(index)
        index = index + 1
        if index < len(tree) and tree[index] is not None:
            stack.append(index)
    return res[::-1]

print(postorder(tree))

## 큐를 이용한 레벨 순서 순회
def levelorder(tree):
    if not tree:
        return []
    res, queue = [], [0]
    
    while queue:
        index = queue.pop(0)
        res.append(tree[index])
        index = 2 * index + 1
        if index < len(tree) and tree[index] is not None:
            queue.append(index)
        index += 1
        if index < len(tree) and tree[index] is not None:
            queue.append(index)
    return res

print(levelorder(tree))