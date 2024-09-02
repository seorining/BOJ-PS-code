x, y, z = map(int, input().split())

money = 0


if (x == y) and (x == z) and (y == z):
    money = 10000 + x * 1000
elif (x != y) and (y != z) and (x != z):
    if (x >= y) and (x >= z):
        max = x
    elif (y >= x)  and (y >= z):
        max = y
    else :
        max = z
        
    money = max * 100
else :
    if (x == y):
        same = x
    elif (x == z):
        same = x
    else:
        same = y 
    money = 1000 +  same * 100
    
print(money)