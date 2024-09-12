import sys

pocketmonNumDict = {}
pocketmonNameDict = {}

n, m = map(int, sys.stdin.readline().rstrip().split())
for i in range(1, n+1):
    pocketmonName = sys.stdin.readline().rstrip()
    pocketmonNumDict[i] = pocketmonName
    pocketmonNameDict[pocketmonName] = i

for _ in range(m):
    query = input()
    if query.isdigit():
        print(pocketmonNumDict[int(query)])
    else:
        print(pocketmonNameDict[query])
        
        
## 딕셔너리가 아니라 리스트에 넣어도 돼...