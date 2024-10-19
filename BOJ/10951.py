
add = []

while True:
    try:
        x, y = map(int, input().split())
            
        add.append(x+y)
    
    except:
        break
    
for i in add:
    print(i)