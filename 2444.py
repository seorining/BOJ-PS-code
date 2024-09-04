x = int(input())

for i in range(x):
    for j in range(x - i - 1):
        print(" ", end="")
    for j in range(2*i + 1):
        print("*", end="")
    print()

for i in range(x-1):
    for j in range(i+1):
        print(" ", end="")
    for j in range(x*2-i*2 - 3):
        print("*", end="")
    print()