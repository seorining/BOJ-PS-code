x = int(input())

for i in range(x):
    for j in range(x*2):
        if i % 2 == 0:
            if j % 2 == 0:
                print("*", end="")
            else:
                print(" ", end="")
        else:
            if j % 2 ==0:
                print(" ", end="")
            else :
                print("*", end="")
    print()
    
