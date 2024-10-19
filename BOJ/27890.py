x, n = map(int, input().split())

for i in range(n):
    if x % 2 ==0:
        x = x // 2
        x = x ^ 6
        pass
    else:
        x = x * 2
        x = x ^ 6
        pass
    
print(x)