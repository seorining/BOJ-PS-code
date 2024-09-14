import sys

n = int(sys.stdin.readline().rstrip())

time_list = [i for i in map(int, sys.stdin.readline().rstrip().split())]

time_list.sort()

sum_all = 0
sum_each = 0
for i in time_list:
    sum_each += i
    sum_all += sum_each
    
print(sum_all)