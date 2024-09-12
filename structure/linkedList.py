#(1: Bulbasaur)

pocketmonNumDict = {}
pocketmonNameDict = {}

n, m = map(int, input().split())
for i in range(1, n+1):
    pocketmonName = input()
    pocketmonNumDict[i] = pocketmonName
    pocketmonNameDict[pocketmonName] = i

for _ in range(m):
    query = input()
    if query.isdigit():
        print(pocketmonNumDict[int(query)])
    else:
        print(pocketmonNameDict[query])