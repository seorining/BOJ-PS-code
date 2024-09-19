input()
number = list(map(int, input().split()))
count = 0

for i in number:
    if i == 2:
        count += 1
    for j in range(2, i):
        if j == i-1:
            count += 1
        if i % j == 0:
            break

print(count)