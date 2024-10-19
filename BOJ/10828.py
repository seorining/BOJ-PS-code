from collections import deque

stack = deque('E')

def pushStack(x):
    stack.append(x)
    
def popStack():
    if len(stack) == 1:
        return print(-1)
    else:
        return print(stack.pop())
    
def sizeStack():
    return print(len(stack) - 1)

def isEmptyStack():
    if len(stack) == 1:
        return print(1)
    else : 
        return print(0)
    
def topStack():
    if len(stack) == 1:
        return print(-1)
    else:
        n = stack.pop()
        stack.append(n)
        return print(n)
    
n = int(input())

opList = [input().split() for i in range(n)]

for op in opList:
    if op[0] == 'push':
        pushStack(int(op[1]))
    elif op[0] == 'pop':
        popStack()
    elif op[0] == 'size':
        sizeStack()
    elif op[0] == 'empty':
        isEmptyStack()
    elif op[0] == 'top':
        topStack()