loop = int(input())

add = list()

for i in range(loop):
    x, y = map(int, input().split())
    add.append(x+y)

for i in add:
    print(i)