def update(target,value):
    target+=size
    while target>0:
        segtree[target]+=value
        target//=2

def pop(k):
    start=1
    while start<=size:
        if segtree[2*start]<k:
            k-=segtree[2*start]
            start=2*start+1
        else:
            start=2*start
    update(start-size,-1)
    return str(start-size)

size = 1<<17
#############################################
segtree = [0] * (size * 2 + 1)
n,k=map(int,input().split())
for i in range(1, n+1):
    update(i, 1)

target = k
printList = []
for i in range(n-1, 0, -1):
    printList.append(pop(target))
    target = (target-2+k) % i + 1
printList.append(pop(1))

print("<"+",".join(printList)+">")