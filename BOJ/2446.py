def star(num):
    for i in range(num):
        print("*", end="")

def blank(num):
    for i in range(num):
        print(" ", end="")

x = int(input())

for i in range(x):
    blank(i)
    star(2*x - 2*i - 1)
    print()
    
for i in range(x-1):
    blank(x-i-2)
    star(2*i+3)
    print()