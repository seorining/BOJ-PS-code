def star(num):
    for i in range(num):
        print("*", end="")

def blank(num):
    for i in range(num):
        print(" ", end="")

x = int(input())

for i in range(x-1):
    star(i+1)
    blank(x*2 - i*2 - 2)
    star(i+1)
    print()
star(2*x)
print()
for i in range(x-1):
    star(x- i -1)
    blank(2*i+2)
    star(x -i -1)
    print()