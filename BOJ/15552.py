import sys

loop = int(sys.stdin.readline())
list = []

for i in range(loop):
    x, y = map(int, sys.stdin.readline().split())
    list.append(x + y)
    
for i in range(loop):
    print(list[i])