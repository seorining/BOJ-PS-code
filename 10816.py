n = int(input())
nList = [i for i in map(int, input().split())]
m = int(input())
mList = [i for i in map(int, input().split())]

printDict = {}

for i in nList:
    if i in printDict:
        printDict[i] += 1
    else:
        printDict[i] = 1
        
for i in mList:
    if i in printDict:
        print(printDict[i], end =' ')
    else:
        print(0, end=' ')