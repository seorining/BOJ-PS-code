verfi = list(map(int, input().split()))

sum = 0
for i in verfi:
    sum += i * i
    
print(sum%10)