x = int(input())

for i in range(x):
    for j in range(x-i-1):
        print(" ", end="")
    print("*", end="")
    if i > 0:
        for j in range(i*2-1):
            print(" ", end="")
        print("*", end="")
    print()