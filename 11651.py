n = int(input())
coodList = []

for i in range(n):
    x, y = map(int, input().split())
    coodList.append([x,y])
    
coodList.sort(key=lambda x: x[0])
coodList.sort(key=lambda x: x[1])

for i in coodList:
    print(f"{i[0]} {i[1]}")