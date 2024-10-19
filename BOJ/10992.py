x = int(input())

for i in range(x-1):
    for j in range(x+i):
        if (j == x + i - 1 or j == x + i - 2*i - 1):
            print("*", end="")
        else:
            print(" ", end="")
    print()
            
for i in range(2*x-1):
    print("*", end="")
print()