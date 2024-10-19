personList = []
rankList = []

for i in range(int(input())):
    x, y = map(int, input().split())
    personList.append([x,y])
    
for x, y in personList:
    rank = 1
    for p, q in personList:
        if x < p and y < q:
            rank += 1
    rankList.append(rank)
    
print(*rankList, sep=' ')