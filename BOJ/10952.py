add = []

while(True):
    x, y = map(int, input().split())
    if x == 0 and y == 0:
        break
    
    add.append(x+y)

for i in add:
    print(i)