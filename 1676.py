n = int(input())

number = 1
for i in range(1,n+1):
    number *= i

count = 0
while True:
    if number % 10 == 0:
        count = count + 1
    else: break
    number = number // 10

print(count)