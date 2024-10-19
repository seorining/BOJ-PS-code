N = int(input())
list = map(int, input().split())
v = int(input())

count = 0

for _ in list:
    if v == _:
        count += 1

print(count)