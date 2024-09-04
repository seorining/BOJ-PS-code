def star(i):
    if i == 1:
        print("*")
    elif i == 2:
        for i in range(3):
            for j in range(i):
                print(" ", end="")
            for j in range(3*2 -2*i-1):
                print("*", end="")
            print("*")

print(star(2))

