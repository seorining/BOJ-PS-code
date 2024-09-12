import sys
input = sys.stdin.readline

setS = set()

def add(n):
    global setS
    setS.add(n)
    
def remove(n):
    global setS
    setS.discard(n)
    
def check(n):
    global setS
    if n in setS:
        print(1)
    else:
        print(0)

def toggle(n):
    global setS
    if n in setS:
        remove(n)
    else:
        add(n)
        
def all():
    global setS
    setS = set([i for i in range(1, 21)])
    
def empty():
    global setS
    setS.clear()
    
    
m = int(input())

for i in range(m):
    op = input().split()
    
    if op[0] == 'add':
        add(int(op[1]))
    elif op[0] =='remove':
        remove(int(op[1]))
    elif op[0] =='check':
        check(int(op[1]))
    elif op[0] =='toggle':
        toggle(int(op[1]))
    elif op[0] =='all':
        all()
    elif op[0] =='empty':
        empty()