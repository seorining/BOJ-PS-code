def Greatest(x,y):
    while y != 0:
        x, y = y, x%y
    return x

x, y = map(int, input().split())

if x < y:
    c = x
    x = y
    y = c

GreatestNum = Greatest(x, y)

LeastNum = GreatestNum * ( x // GreatestNum) * ( y // GreatestNum )

print(GreatestNum)
print(LeastNum)