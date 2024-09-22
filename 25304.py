price_all = int(input())

n = int(input())

sum = 0
for _ in range(n):
    price, count = map(int, input().split())
    sum += price * count
    
print("Yes") if sum == price_all else print("No")