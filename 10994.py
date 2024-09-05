x = int(input())

pos = (4*x - 3) // 2

def firstStar(n):
    for i in range(n):
        if i % 2 == 0:
            print("*", end="")
        else:
            print(" ", end="")

def firstBlank(n):
    for i in range(n):
        if i % 2 == 0:
            print(" ", end="")
        else:
            print("*", end="")
            
def drawStar(n):
    for i in range(n):
        print("*", end="")

def drawBlank(n):
    for i in range(n):
        print(" ",end="")

for i in range(2*pos + 1):
    if i <= pos:
        if i % 2 == 0:
            firstStar(i)
            drawStar((2*pos+1) - 4*(i//2))
            firstBlank(i)
        else:
            firstStar(i)
            drawBlank((2*pos-1) - 4*(i//2))
            firstStar(i)
    else:
        i = i - pos
        if i % 2 == 0:
            firstStar(pos- 2*(i//2))
            drawStar(4 * (i//2) + 1)
            firstBlank(pos-2*(i//2))
        else:
            firstStar(pos - 1 - 2*(i//2))
            drawBlank(4* (i//2) + 3)
            firstStar(pos - 1 - 2*(i//2))
    print()    