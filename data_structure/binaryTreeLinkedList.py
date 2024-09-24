class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
class Tree:
    def __init__(self):
        self.root = None
        
    def makeTree(self, arr):
        if not arr:
            return
        self.root = Node(arr[0])
        queue = [self.root]
        index = 1
        while queue and index < len(arr):
            node = queue.pop(0)
            if index < len(arr) and arr[index] is not None:
                node.left = Node(arr[index])
                queue.append(node.left)
            index += 1
            if index < len(arr) and arr[index] is not None:
                node.right = Node(arr[index])
                queue.append(node.right)
            index += 1
        
    def preorder(self):
        def _preorder(node):
            if node is None:
                return
            res.append(node.data)
            _preorder(node.left)
            _preorder(node.right)

        res = []
        _preorder(self.root)
        return res
    
    def inorder(self):
        def _inorder(node):
            if node is None:
                return
            _inorder(node.left)
            res.append(node.data)
            _inorder(node.right)

        res = []
        _inorder(self.root)
        return res
            
    def postorder(self):
        def _postorder(node):
            if node is None:
                return
            _postorder(node.left)
            _postorder(node.right)
            res.append(node.data)

        res = []
        _postorder(self.root)
        return res
    
    def levelorder(self):
        res = []
        if not self.root:
            return res
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            res.append(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
        return res
    
def insertKey(tree, key):
    newNode = Node(key)
    if not tree.root:
        tree.root = newNode
    else:
        queue = [tree.root]
        while queue:
            node = queue.pop(0)
            if node.left is None:
                node.left = newNode
                break
            else:
                queue.append(node.left)
            if node.right is None:
                node.right = newNode
                break
            else:
                queue.append(node.right)

def deleteKey(tree, key):
    if tree.root is None:
        return
    queue = [(tree.root, tree.root)]    #(노드, 부모 노드)
    deleteNode = None
    
    while queue:
        node, lastParent = queue.pop(0)
        lastNodeData = node.data
        if node.data == key:
            deleteNode = node
        if node.left:
            queue.append((node.left, node))
        if node.right:
            queue.append((node.right, node))
    
    if deleteNode is None:
        print(f"There is not {key}")
        
    deleteNode.data = lastNodeData
    if lastParent.right is not None:
        lastParent.right = None
    elif lastParent.left is not None:
        lastParent.left = None
    else:
        tree.root = None
        
def findHasNoSibling(tree):
    res, q = [], [tree.root]
    while q:
        node = q.pop(0)
        if node.left:
            q.append(node.left)
            if not node.right:
                res.append(node.left.data)
                continue
        if node.right:
            q.append(node.right)
            if not node.left:
                res.append(node.right.data)
                continue
    return res if res else [-1]

if __name__ == "__main__":
    tree = Tree()
    tree.makeTree([13, 12, 10, 4, 19, 16, 9])
    print(tree.levelorder())
    deleteKey(tree, 9)
    print(tree.levelorder())
    deleteKey(tree, 13)
    print(tree.levelorder())
    deleteKey(tree, 12)
    print(tree.levelorder())
    deleteKey(tree, 4)
    print(tree.levelorder())
    deleteKey(tree, 19)
    print(tree.levelorder())
    deleteKey(tree, 10)
    print(tree.levelorder())
    deleteKey(tree, 16)
    print(tree.levelorder())
    deleteKey(tree, 16)
    print(tree.levelorder())