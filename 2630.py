import sys

def checkPaper(x,y,length):
    if length == 1:
        if paper[y][x] == 1:
            color[1] += 1
            return
        elif paper[y][x] == 0:
            color[0] += 1
            return
    
    check_white = False
    check_blue = False
    
    if paper[y][x] == 1:
        check_blue = True
        for i in range(length):
            for j in range(length):
                if paper[y+i][x+j] == 0:
                    check_blue = False
                    break
    else:
        check_white = True
        for i in range(length):
            for j in range(length):
                if paper[y+i][x+j] == 1:
                    check_white = False
                    break
    
    if check_blue:
        color[1] += 1
        return
    elif check_white:
        color[0] += 1
        return
    else:
        checkPaper(x, y, length//2)
        checkPaper(x+length//2, y, length//2)
        checkPaper(x, y+length//2, length//2)
        checkPaper(x+length//2, y+length//2, length//2)
        

n = int(sys.stdin.readline())

paper = []
color = [0, 0]

for _ in range(n):
    paper.append(list(map(int, sys.stdin.readline().split())))

checkPaper(0,0,n)

print(color[0])
print(color[1])