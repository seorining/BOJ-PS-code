import sys

n, m = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))

sum_list=[0]
sum = 0
for i in num_list:
    sum += i
    sum_list.append(sum)
    
for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    print(sum_list[y] - sum_list[x-1])