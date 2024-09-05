x = int(input())

for i in range(2*x):
    print(*["*" if ~j&1 else " " for j in range(x)],sep='') if ~i&1 else print(*["*" if j&1 else " " for j in range(x)],sep='')