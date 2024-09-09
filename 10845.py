from collections import deque

queue = deque()

def pushQueue(n):
    queue.append(n)

def popQueue():
    if len(queue) == 0:
        print(-1)
    else:
        return print(queue.popleft())
    
def sizeQueue():
    return print(len(queue))

def isEmptyQueue():
    if len(queue) == 0:
        return print(1)
    else:
        return print(0)
    
def frontQueue():
    if len(queue) == 0:
        return print(-1)
    else:
        n = queue.popleft()
        queue.appendleft(n)
        return print(n)

def backQueue():
    if len(queue) == 0:
        return print(-1)
    else:
        n = queue.pop()
        queue.append(n)
        return print(n)
    
n = int(input())

opList = [input().split() for i in range(n)]

for op in opList:
    if op[0] == 'push':
        pushQueue(int(op[1]))
    elif op[0] == 'pop':
        popQueue()
    elif op[0] == 'size':
        sizeQueue()
    elif op[0] == 'empty':
        isEmptyQueue()
    elif op[0] == 'front':
        frontQueue()
    elif op[0] == 'back':
        backQueue()